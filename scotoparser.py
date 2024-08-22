import os
from itertools import product

import numpy as np
import xslha


def read_spheno_output(spheno_ouput: os.PathLike) -> dict:

    spc = xslha.read(spheno_ouput)

    id_dict = {
        # MG5_ID : Spheno_ID
        "25": 25,  # h
        "135": 1111,  # h2
        "136": 1002,  # eta I
        "137": 1001,  # eta R
        "138": 1003,  # eta p
        "350": 3001,  # N1
        "351": 3002,  # N2
        "352": 3003,  # N3
    }

    mass_names_dict = {
        # MG5_ID : MG5_key
        "25": "Mh1",  # h
        "135": "Mh2",  # h2
        "136": "METAI",  # eta I
        "137": "METAR",  # eta R
        "138": "METAP",  # eta p
        "350": "MN1",  # N1
        "351": "MN2",  # N2
        "352": "MN3",  # N3
    }

    widths_names_dict = {
        # MG5_ID : MG5_key
        "25": "Wh1",  # h
        "135": "Wh2",  # h2
        "136": "WETAI",  # eta I
        "137": "WETAR",  # eta R
        "138": "WETAP",  # eta p
        "350": "WN1",  # N1
        "351": "WN2",  # N2
        "352": "WN3",  # N3
    }

    widths_dict = {
        # MG5_key : Spheno_value
        widths_names_dict[k]: spc.widths.get(v, 0)
        for k, v in id_dict.items()
    }

    mass_dict = {
        # MG5_key : Spheno_value
        mass_names_dict[k]: spc.blocks["MASS"].get(str(v))
        for k, v in id_dict.items()
    }
    # [print(f"{k} : {v}") for k, v in mass_dict.items()]

    YnRE_dict = {
        # MG5_key : Spheno_value
        f"YnRE{i}x{j}": spc.blocks["COUPLINGSYN"].get(f"{i},{j}")
        for i, j in product(range(1, 4), repeat=2)
    }

    YnIMG_dict = {
        # MG5_key : Spheno_value
        f"YnIMG{i}x{j}": spc.blocks["IMCOUPLINGSYN"].get(f"{i},{j}")
        for i, j in product(range(1, 4), repeat=2)
    }

    potential_dict = {
        # MG5_key: Spheno_value
        "muEta": np.sqrt(spc.blocks["HDM"].get("9")),
        "lam1": spc.blocks["SM"].get("2"),
        "lam2": spc.blocks["HDM"].get("2"),
        "lam3": spc.blocks["HDM"].get("3"),
        "vevSig": spc.blocks["HDM"].get("11"),
    }

    unified_dict = {**mass_dict, **widths_dict, **YnRE_dict, **YnIMG_dict, **potential_dict}

    return unified_dict


if __name__ == "__main__":
    spheno_ouput = os.path.join(os.path.dirname(__file__), "test.dat")
    unified_dict = read_spheno_output(spheno_ouput)

    lista = [f"set {key.upper()} {value}\n" for key, value in unified_dict.items()]
