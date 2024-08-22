import os
import random
import shutil
from io import StringIO
from subprocess import Popen

import pandas as pd

from scotoparser import read_spheno_output


def calculate_xs(
    process: str,
    params_dict: dict,
    outputs_dir: os.PathLike,
    ufo_path: os.PathLike,
    mg5_bin_path: os.PathLike,
    n_events: int = 1000,
    n_workers: int = 4,
    sde_strategy: bool = False,  # true for approx strategy, false for exact strategy
    jpeg: bool = False,
    seed: int = 0,  # 0 for auto seed
) -> dict:
    # create a random directory to store the output
    output_dir = os.path.join(outputs_dir, str(random.randint(0, 1000000)))
    try:
        os.makedirs(output_dir)
    except FileExistsError:
        shutil.rmtree(output_dir)
        os.makedirs(output_dir)

    process_file = os.path.join(os.path.dirname(__file__), "process.mg5")
    with open(process_file, "w") as f:
        f.write(f"import model {ufo_path}\n")
        f.write(f"{process}\n")

        if jpeg:
            f.write(f"output {output_dir}\n")
        else:
            f.write(f"output {output_dir} -nojpeg\n")

        f.write(f"launch {output_dir} -m\n")
        f.write(f"{n_workers}\n")
        [f.write(f"set {key.upper()} {value}\n") for key, value in params_dict.items()]
        f.write(f"set iseed {seed}\n")
        f.write(f"set nevents {n_events}\n")
        sde = 0 if sde_strategy else 1
        f.write(f"set sde_strategy {sde}\n")
        f.write("done\n")

    Popen([mg5_bin_path, process_file]).wait()
    shutil.copy(process_file, output_dir)

    # Get the cross section from the html file
    with open(os.path.join(output_dir, "crossx.html")) as f:
        html_string = f.read()
    t = pd.read_html(StringIO(html_string))[0]
    try:
        xs = float(t["Cross section (pb)"][0].split(" ")[0])
    except ValueError:
        xs = 0.0
    return xs


if __name__ == "__main__":
    # search for the .dat files in a specific directory

    directory = "test/Examples"

    model_path = os.path.join(os.path.dirname(__file__), "Scoto_Singlet_Doublet_UFO")

    process = """
    define p = p b b~
    generate p p > eta+ eta-
    """
    mg5_bin_path = os.path.join(os.sep, "Collider", "MG5_aMC_v3_1_0", "bin", "mg5_aMC")

    paths = [
        os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".dat")
    ]

    param_dicts = [
        # filename : unified_dict
        read_spheno_output(path)
        for path in paths
    ]

    xs_list = []

    for param_dict in param_dicts:
        xs = calculate_xs(
            process, param_dict, "outputs", model_path, mg5_bin_path, n_events=int(1e4)
        )
        xs_list.append((param_dict.get("METAI"), xs))

    print(xs_list)
