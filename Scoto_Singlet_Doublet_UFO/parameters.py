# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Linux x86 (64-bit) (December 13, 2023)
# Date: Wed 19 Jun 2024 15:43:44



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

YnRE1x1 = Parameter(name = 'YnRE1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.0037367,
                    texname = '\\text{YnRE1x1}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 1, 1 ])

YnRE1x2 = Parameter(name = 'YnRE1x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.0040789,
                    texname = '\\text{YnRE1x2}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 1, 2 ])

YnRE1x3 = Parameter(name = 'YnRE1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.0027013,
                    texname = '\\text{YnRE1x3}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 1, 3 ])

YnRE2x1 = Parameter(name = 'YnRE2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.0154741,
                    texname = '\\text{YnRE2x1}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 2, 1 ])

YnRE2x2 = Parameter(name = 'YnRE2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.0128888,
                    texname = '\\text{YnRE2x2}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 2, 2 ])

YnRE2x3 = Parameter(name = 'YnRE2x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.0003451,
                    texname = '\\text{YnRE2x3}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 2, 3 ])

YnRE3x1 = Parameter(name = 'YnRE3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.0233544,
                    texname = '\\text{YnRE3x1}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 3, 1 ])

YnRE3x2 = Parameter(name = 'YnRE3x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.0150242,
                    texname = '\\text{YnRE3x2}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 3, 2 ])

YnRE3x3 = Parameter(name = 'YnRE3x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.0114565,
                    texname = '\\text{YnRE3x3}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 3, 3 ])

ggh = Parameter(name = 'ggh',
                nature = 'external',
                type = 'real',
                value = 0.003239,
                texname = 'g_{\\text{ggH}}',
                lhablock = 'EFFECTIVECOUPLINGS',
                lhacode = [ 1 ])

YnIMG1x1 = Parameter(name = 'YnIMG1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.0004669,
                     texname = '\\text{YnIMG1x1}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 1, 1 ])

YnIMG1x2 = Parameter(name = 'YnIMG1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.0069553,
                     texname = '\\text{YnIMG1x2}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 1, 2 ])

YnIMG1x3 = Parameter(name = 'YnIMG1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.0090017,
                     texname = '\\text{YnIMG1x3}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 1, 3 ])

YnIMG2x1 = Parameter(name = 'YnIMG2x1',
                     nature = 'external',
                     type = 'real',
                     value = -0.0000596,
                     texname = '\\text{YnIMG2x1}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 2, 1 ])

YnIMG2x2 = Parameter(name = 'YnIMG2x2',
                     nature = 'external',
                     type = 'real',
                     value = -0.0011498,
                     texname = '\\text{YnIMG2x2}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 2, 2 ])

YnIMG2x3 = Parameter(name = 'YnIMG2x3',
                     nature = 'external',
                     type = 'real',
                     value = -0.0011498,
                     texname = '\\text{YnIMG2x3}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 2, 3 ])

YnIMG3x1 = Parameter(name = 'YnIMG3x1',
                     nature = 'external',
                     type = 'real',
                     value = -0.0019802,
                     texname = '\\text{YnIMG3x1}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 3, 1 ])

YnIMG3x2 = Parameter(name = 'YnIMG3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.0211322,
                     texname = '\\text{YnIMG3x2}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 3, 2 ])

YnIMG3x3 = Parameter(name = 'YnIMG3x3',
                     nature = 'external',
                     type = 'real',
                     value = -0.0381763,
                     texname = '\\text{YnIMG3x3}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 3, 3 ])

muEta = Parameter(name = 'muEta',
                  nature = 'external',
                  type = 'real',
                  value = 500.,
                  texname = '\\mu _{\\eta }',
                  lhablock = 'SCALARPOTBLOCK',
                  lhacode = [ 1 ])

lam1 = Parameter(name = 'lam1',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _1',
                 lhablock = 'SCALARPOTBLOCK',
                 lhacode = [ 2 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _2',
                 lhablock = 'SCALARPOTBLOCK',
                 lhacode = [ 3 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _3',
                 lhablock = 'SCALARPOTBLOCK',
                 lhacode = [ 4 ])

vevSig = Parameter(name = 'vevSig',
                   nature = 'external',
                   type = 'real',
                   value = 6386,
                   texname = '\\text{vevSig}',
                   lhablock = 'SCALARPOTBLOCK',
                   lhacode = [ 5 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MN1 = Parameter(name = 'MN1',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{MN1}',
                lhablock = 'MASS',
                lhacode = [ 350 ])

MN2 = Parameter(name = 'MN2',
                nature = 'external',
                type = 'real',
                value = 0.2,
                texname = '\\text{MN2}',
                lhablock = 'MASS',
                lhacode = [ 351 ])

MN3 = Parameter(name = 'MN3',
                nature = 'external',
                type = 'real',
                value = 0.3,
                texname = '\\text{MN3}',
                lhablock = 'MASS',
                lhacode = [ 352 ])

Mh1 = Parameter(name = 'Mh1',
                nature = 'external',
                type = 'real',
                value = 125.074,
                texname = '\\text{Mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

Mh2 = Parameter(name = 'Mh2',
                nature = 'external',
                type = 'real',
                value = 246.07,
                texname = '\\text{Mh2}',
                lhablock = 'MASS',
                lhacode = [ 135 ])

METAI = Parameter(name = 'METAI',
                  nature = 'external',
                  type = 'real',
                  value = 471.21,
                  texname = '\\text{METAI}',
                  lhablock = 'MASS',
                  lhacode = [ 136 ])

METAR = Parameter(name = 'METAR',
                  nature = 'external',
                  type = 'real',
                  value = 471.35,
                  texname = '\\text{METAR}',
                  lhablock = 'MASS',
                  lhacode = [ 137 ])

METAP = Parameter(name = 'METAP',
                  nature = 'external',
                  type = 'real',
                  value = 471.28,
                  texname = '\\text{METAP}',
                  lhablock = 'MASS',
                  lhacode = [ 138 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 0.01,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 350 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 0.02,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 351 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 0.03,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 352 ])

Wh1 = Parameter(name = 'Wh1',
                nature = 'external',
                type = 'real',
                value = 0.00638,
                texname = '\\text{Wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

Wh2 = Parameter(name = 'Wh2',
                nature = 'external',
                type = 'real',
                value = 1.3667,
                texname = '\\text{Wh2}',
                lhablock = 'DECAY',
                lhacode = [ 135 ])

WETAI = Parameter(name = 'WETAI',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{WETAI}',
                  lhablock = 'DECAY',
                  lhacode = [ 136 ])

WETAR = Parameter(name = 'WETAR',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{WETAR}',
                  lhablock = 'DECAY',
                  lhacode = [ 137 ])

WETAP = Parameter(name = 'WETAP',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{WETAP}',
                  lhablock = 'DECAY',
                  lhacode = [ 138 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

muEta2 = Parameter(name = 'muEta2',
                   nature = 'internal',
                   type = 'real',
                   value = 'muEta**2',
                   texname = '\\mu ^2{}_{\\eta }')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

vev2 = Parameter(name = 'vev2',
                 nature = 'internal',
                 type = 'real',
                 value = '0',
                 texname = '\\text{vev2}')

YN1 = Parameter(name = 'YN1',
                nature = 'internal',
                type = 'real',
                value = 'MN1/(vevSig*cmath.sqrt(2))',
                texname = '\\text{YN1}')

YN2 = Parameter(name = 'YN2',
                nature = 'internal',
                type = 'real',
                value = 'MN2/(vevSig*cmath.sqrt(2))',
                texname = '\\text{YN2}')

YN3 = Parameter(name = 'YN3',
                nature = 'internal',
                type = 'real',
                value = 'MN3/(vevSig*cmath.sqrt(2))',
                texname = '\\text{YN3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

vev1 = Parameter(name = 'vev1',
                 nature = 'internal',
                 type = 'real',
                 value = 'vev',
                 texname = '\\text{vev1}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

lam3EtaSig = Parameter(name = 'lam3EtaSig',
                       nature = 'internal',
                       type = 'real',
                       value = '(2*(METAP**2 - muEta2) - lam3*vev1**2)/vevSig**2',
                       texname = '\\lambda _{3 \\text{$\\eta $S}}')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*(METAI**2 - 2*METAP**2 + METAR**2))/vev1**2',
                 texname = '\\lambda _4')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'real',
                 value = '(-METAI**2 + METAR**2)/vev1**2',
                 texname = '\\lambda _5')

lamSig = Parameter(name = 'lamSig',
                   nature = 'internal',
                   type = 'real',
                   value = '(Mh1**2 + Mh2**2 - lam1*vev1**2)/vevSig**2',
                   texname = '\\lambda _S')

lam3HSig = Parameter(name = 'lam3HSig',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cmath.sqrt((-Mh1**2 + Mh2**2)**2 - (lam1*vev1**2 - lamSig*vevSig**2)**2)/(2.*vev1*vevSig)',
                     texname = '\\lambda _{3 \\text{HS}}')

muH2 = Parameter(name = 'muH2',
                 nature = 'internal',
                 type = 'complex',
                 value = '(-(lam1*vev1**2) - lam3HSig*vevSig**2)/2.',
                 texname = '\\mu ^2{}_H')

muS2 = Parameter(name = 'muS2',
                 nature = 'internal',
                 type = 'complex',
                 value = '(-(lam3HSig*vev1**2) - lamSig*vevSig**2)/2.',
                 texname = '\\mu ^2{}_S')

tga = Parameter(name = 'tga',
                nature = 'internal',
                type = 'complex',
                value = '(2*lam3HSig*vev1*vevSig)/(Mh1**2 - Mh2**2 + lam1*vev1**2 - lamSig*vevSig**2)',
                texname = '\\{\\tan (\\alpha )\\}')

alpha = Parameter(name = 'alpha',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.atan(tga)',
                  texname = '\\alpha')

ca = Parameter(name = 'ca',
               nature = 'internal',
               type = 'complex',
               value = 'cmath.cos(alpha)',
               texname = 'c_{\\alpha }')

sa = Parameter(name = 'sa',
               nature = 'internal',
               type = 'complex',
               value = 'cmath.sin(alpha)',
               texname = 's_{\\alpha }')

