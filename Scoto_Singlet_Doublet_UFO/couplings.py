# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Linux x86 (64-bit) (December 13, 2023)
# Date: Wed 19 Jun 2024 15:43:45


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-0.5*ee**2/cw',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*lam2)',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-2*complex(0,1)*lam2',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-3*complex(0,1)*lam2',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-0.5*ee/sw',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-0.5*ee**2/sw',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-0.5*(cw*ee)/sw - (ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(-3*complex(0,1)*Mh1**2)/vevSig**2 - (3*complex(0,1)*Mh2**2)/vevSig**2 + (3*complex(0,1)*lam1*vev**2)/vevSig**2',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(-2*complex(0,1)*METAP**2)/vevSig**2 + (2*complex(0,1)*muEta**2)/vevSig**2 + (complex(0,1)*lam3*vev**2)/vevSig**2',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = 'complex(0,1)*YnIMG1x1 - YnRE1x1',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = 'complex(0,1)*YnIMG1x1 + YnRE1x1',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(complex(0,1)*YnIMG1x1)/cmath.sqrt(2) - YnRE1x1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(YnIMG1x1/cmath.sqrt(2)) - (complex(0,1)*YnRE1x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'YnIMG1x1/cmath.sqrt(2) - (complex(0,1)*YnRE1x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(complex(0,1)*YnIMG1x1)/cmath.sqrt(2) + YnRE1x1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = 'complex(0,1)*YnIMG1x2 - YnRE1x2',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = 'complex(0,1)*YnIMG1x2 + YnRE1x2',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(complex(0,1)*YnIMG1x2)/cmath.sqrt(2) - YnRE1x2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(YnIMG1x2/cmath.sqrt(2)) - (complex(0,1)*YnRE1x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = 'YnIMG1x2/cmath.sqrt(2) - (complex(0,1)*YnRE1x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(complex(0,1)*YnIMG1x2)/cmath.sqrt(2) + YnRE1x2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'complex(0,1)*YnIMG1x3 - YnRE1x3',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'complex(0,1)*YnIMG1x3 + YnRE1x3',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(complex(0,1)*YnIMG1x3)/cmath.sqrt(2) - YnRE1x3/cmath.sqrt(2)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(YnIMG1x3/cmath.sqrt(2)) - (complex(0,1)*YnRE1x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'YnIMG1x3/cmath.sqrt(2) - (complex(0,1)*YnRE1x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(complex(0,1)*YnIMG1x3)/cmath.sqrt(2) + YnRE1x3/cmath.sqrt(2)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'complex(0,1)*YnIMG2x1 - YnRE2x1',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = 'complex(0,1)*YnIMG2x1 + YnRE2x1',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(complex(0,1)*YnIMG2x1)/cmath.sqrt(2) - YnRE2x1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(YnIMG2x1/cmath.sqrt(2)) - (complex(0,1)*YnRE2x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = 'YnIMG2x1/cmath.sqrt(2) - (complex(0,1)*YnRE2x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(complex(0,1)*YnIMG2x1)/cmath.sqrt(2) + YnRE2x1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'complex(0,1)*YnIMG2x2 - YnRE2x2',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = 'complex(0,1)*YnIMG2x2 + YnRE2x2',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(complex(0,1)*YnIMG2x2)/cmath.sqrt(2) - YnRE2x2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(YnIMG2x2/cmath.sqrt(2)) - (complex(0,1)*YnRE2x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'YnIMG2x2/cmath.sqrt(2) - (complex(0,1)*YnRE2x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(complex(0,1)*YnIMG2x2)/cmath.sqrt(2) + YnRE2x2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'complex(0,1)*YnIMG2x3 - YnRE2x3',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = 'complex(0,1)*YnIMG2x3 + YnRE2x3',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(complex(0,1)*YnIMG2x3)/cmath.sqrt(2) - YnRE2x3/cmath.sqrt(2)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(YnIMG2x3/cmath.sqrt(2)) - (complex(0,1)*YnRE2x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'YnIMG2x3/cmath.sqrt(2) - (complex(0,1)*YnRE2x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(complex(0,1)*YnIMG2x3)/cmath.sqrt(2) + YnRE2x3/cmath.sqrt(2)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'complex(0,1)*YnIMG3x1 - YnRE3x1',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = 'complex(0,1)*YnIMG3x1 + YnRE3x1',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(complex(0,1)*YnIMG3x1)/cmath.sqrt(2) - YnRE3x1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(YnIMG3x1/cmath.sqrt(2)) - (complex(0,1)*YnRE3x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = 'YnIMG3x1/cmath.sqrt(2) - (complex(0,1)*YnRE3x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(complex(0,1)*YnIMG3x1)/cmath.sqrt(2) + YnRE3x1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = 'complex(0,1)*YnIMG3x2 - YnRE3x2',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'complex(0,1)*YnIMG3x2 + YnRE3x2',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(complex(0,1)*YnIMG3x2)/cmath.sqrt(2) - YnRE3x2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(YnIMG3x2/cmath.sqrt(2)) - (complex(0,1)*YnRE3x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = 'YnIMG3x2/cmath.sqrt(2) - (complex(0,1)*YnRE3x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(complex(0,1)*YnIMG3x2)/cmath.sqrt(2) + YnRE3x2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'complex(0,1)*YnIMG3x3 - YnRE3x3',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = 'complex(0,1)*YnIMG3x3 + YnRE3x3',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(complex(0,1)*YnIMG3x3)/cmath.sqrt(2) - YnRE3x3/cmath.sqrt(2)',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(YnIMG3x3/cmath.sqrt(2)) - (complex(0,1)*YnRE3x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = 'YnIMG3x3/cmath.sqrt(2) - (complex(0,1)*YnRE3x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(complex(0,1)*YnIMG3x3)/cmath.sqrt(2) + YnRE3x3/cmath.sqrt(2)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(4*complex(0,1)*ggh*cmath.cos(alpha))/vev',
                  order = {'HGG':1,'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(4*G*ggh*cmath.cos(alpha))/vev',
                  order = {'HGG':1,'QCD':1,'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(-4*complex(0,1)*G**2*ggh*cmath.cos(alpha))/vev',
                  order = {'HGG':1,'QCD':2,'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(ee**2*complex(0,1)*vev*cmath.cos(alpha))/(2.*sw**2)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((complex(0,1)*yb*cmath.cos(alpha))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-2*complex(0,1)*YN1*cmath.cos(alpha)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-2*complex(0,1)*YN2*cmath.cos(alpha)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-2*complex(0,1)*YN3*cmath.cos(alpha)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((complex(0,1)*yt*cmath.cos(alpha))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((complex(0,1)*ytau*cmath.cos(alpha))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ee**2*complex(0,1)*cmath.cos(alpha)**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = 'ee**2*complex(0,1)*vev*cmath.cos(alpha) + (cw**2*ee**2*complex(0,1)*vev*cmath.cos(alpha))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev*cmath.cos(alpha))/(2.*cw**2)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-0.5*(complex(0,1)*lam3*vev*cmath.cos(alpha)) - (2*complex(0,1)*METAP**2*cmath.cos(alpha))/vevSig + (2*complex(0,1)*muEta**2*cmath.cos(alpha))/vevSig + (complex(0,1)*lam3*vev**2*cmath.cos(alpha))/vevSig',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(-2*complex(0,1)*METAI**2*cmath.cos(alpha))/vev + (2*complex(0,1)*METAP**2*cmath.cos(alpha))/vev - (complex(0,1)*lam3*vev*cmath.cos(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.cos(alpha))/vevSig + (2*complex(0,1)*muEta**2*cmath.cos(alpha))/vevSig + (complex(0,1)*lam3*vev**2*cmath.cos(alpha))/vevSig',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(2*complex(0,1)*METAP**2*cmath.cos(alpha))/vev - (2*complex(0,1)*METAR**2*cmath.cos(alpha))/vev - (complex(0,1)*lam3*vev*cmath.cos(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.cos(alpha))/vevSig + (2*complex(0,1)*muEta**2*cmath.cos(alpha))/vevSig + (complex(0,1)*lam3*vev**2*cmath.cos(alpha))/vevSig',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((complex(0,1)*Mh1**2*cmath.cos(alpha))/vevSig) - (complex(0,1)*Mh2**2*cmath.cos(alpha))/vevSig + (complex(0,1)*lam1*vev**2*cmath.cos(alpha))/vevSig + (cmath.cos(alpha)*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2))/vevSig',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = 'ee**2*complex(0,1)*cmath.cos(alpha)**2 + (cw**2*ee**2*complex(0,1)*cmath.cos(alpha)**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*cmath.cos(alpha)**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.5*(complex(0,1)*lam3*cmath.cos(alpha)**2) - (2*complex(0,1)*METAP**2*cmath.cos(alpha)**2)/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.cos(alpha)**2)/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.cos(alpha)**2)/vevSig**2',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '-0.5*(complex(0,1)*lam3*cmath.cos(alpha)**2) - (2*complex(0,1)*METAI**2*cmath.cos(alpha)**2)/vev**2 + (2*complex(0,1)*METAP**2*cmath.cos(alpha)**2)/vev**2 - (2*complex(0,1)*METAP**2*cmath.cos(alpha)**2)/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.cos(alpha)**2)/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.cos(alpha)**2)/vevSig**2',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-0.5*(complex(0,1)*lam3*cmath.cos(alpha)**2) + (2*complex(0,1)*METAP**2*cmath.cos(alpha)**2)/vev**2 - (2*complex(0,1)*METAR**2*cmath.cos(alpha)**2)/vev**2 - (2*complex(0,1)*METAP**2*cmath.cos(alpha)**2)/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.cos(alpha)**2)/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.cos(alpha)**2)/vevSig**2',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((complex(0,1)*Mh1**2*cmath.cos(alpha)**2)/vevSig**2) - (complex(0,1)*Mh2**2*cmath.cos(alpha)**2)/vevSig**2 + (complex(0,1)*lam1*vev**2*cmath.cos(alpha)**2)/vevSig**2 + (cmath.cos(alpha)**2*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2))/(vev*vevSig)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-3*complex(0,1)*lam1*vev*cmath.cos(alpha)**3 - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)**3)/vevSig - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)**3)/vevSig + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)**3)/vevSig + (3*cmath.cos(alpha)**3*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2))/vev + (3*cmath.cos(alpha)**3*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2))/vevSig',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-3*complex(0,1)*lam1*cmath.cos(alpha)**4 - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)**4)/vevSig**2 - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)**4)/vevSig**2 + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)**4)/vevSig**2 + (6*cmath.cos(alpha)**4*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2))/(vev*vevSig)',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(4*complex(0,1)*ggh*cmath.sin(alpha))/vev',
                  order = {'HGG':1,'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(4*G*ggh*cmath.sin(alpha))/vev',
                  order = {'HGG':1,'QCD':1,'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(-4*complex(0,1)*G**2*ggh*cmath.sin(alpha))/vev',
                  order = {'HGG':1,'QCD':2,'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-0.5*(ee**2*complex(0,1)*vev*cmath.sin(alpha))/sw**2',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(complex(0,1)*yb*cmath.sin(alpha))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-2*complex(0,1)*YN1*cmath.sqrt(2)*cmath.sin(alpha)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-2*complex(0,1)*YN2*cmath.sqrt(2)*cmath.sin(alpha)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-2*complex(0,1)*YN3*cmath.sqrt(2)*cmath.sin(alpha)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(complex(0,1)*yt*cmath.sin(alpha))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(complex(0,1)*ytau*cmath.sin(alpha))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-0.5*(ee**2*complex(0,1)*cmath.cos(alpha)*cmath.sin(alpha))/sw**2',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee**2*complex(0,1)*cmath.sin(alpha)**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(ee**2*complex(0,1)*vev*cmath.sin(alpha)) - (cw**2*ee**2*complex(0,1)*vev*cmath.sin(alpha))/(2.*sw**2) - (ee**2*complex(0,1)*sw**2*vev*cmath.sin(alpha))/(2.*cw**2)',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(complex(0,1)*lam3*vev*cmath.sin(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.sin(alpha))/vevSig + (2*complex(0,1)*muEta**2*cmath.sin(alpha))/vevSig + (complex(0,1)*lam3*vev**2*cmath.sin(alpha))/vevSig',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(2*complex(0,1)*METAI**2*cmath.sin(alpha))/vev - (2*complex(0,1)*METAP**2*cmath.sin(alpha))/vev + (complex(0,1)*lam3*vev*cmath.sin(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.sin(alpha))/vevSig + (2*complex(0,1)*muEta**2*cmath.sin(alpha))/vevSig + (complex(0,1)*lam3*vev**2*cmath.sin(alpha))/vevSig',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(-2*complex(0,1)*METAP**2*cmath.sin(alpha))/vev + (2*complex(0,1)*METAR**2*cmath.sin(alpha))/vev + (complex(0,1)*lam3*vev*cmath.sin(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.sin(alpha))/vevSig + (2*complex(0,1)*muEta**2*cmath.sin(alpha))/vevSig + (complex(0,1)*lam3*vev**2*cmath.sin(alpha))/vevSig',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((complex(0,1)*Mh1**2*cmath.sin(alpha))/vevSig) - (complex(0,1)*Mh2**2*cmath.sin(alpha))/vevSig + (complex(0,1)*lam1*vev**2*cmath.sin(alpha))/vevSig - (cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha))/vevSig',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(ee**2*complex(0,1)*cmath.cos(alpha)*cmath.sin(alpha)) - (cw**2*ee**2*complex(0,1)*cmath.cos(alpha)*cmath.sin(alpha))/(2.*sw**2) - (ee**2*complex(0,1)*sw**2*cmath.cos(alpha)*cmath.sin(alpha))/(2.*cw**2)',
                  order = {'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(complex(0,1)*lam3*cmath.cos(alpha)*cmath.sin(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '(complex(0,1)*lam3*cmath.cos(alpha)*cmath.sin(alpha))/2. + (2*complex(0,1)*METAI**2*cmath.cos(alpha)*cmath.sin(alpha))/vev**2 - (2*complex(0,1)*METAP**2*cmath.cos(alpha)*cmath.sin(alpha))/vev**2 - (2*complex(0,1)*METAP**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '(complex(0,1)*lam3*cmath.cos(alpha)*cmath.sin(alpha))/2. - (2*complex(0,1)*METAP**2*cmath.cos(alpha)*cmath.sin(alpha))/vev**2 + (2*complex(0,1)*METAR**2*cmath.cos(alpha)*cmath.sin(alpha))/vev**2 - (2*complex(0,1)*METAP**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((complex(0,1)*Mh1**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2) - (complex(0,1)*Mh2**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 + (complex(0,1)*lam1*vev**2*cmath.cos(alpha)*cmath.sin(alpha))/vevSig**2 - (cmath.cos(alpha)*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha))/(vev*vevSig)',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '3*complex(0,1)*lam1*vev*cmath.cos(alpha)**2*cmath.sin(alpha) - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)**2*cmath.sin(alpha))/vevSig - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)**2*cmath.sin(alpha))/vevSig + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)**2*cmath.sin(alpha))/vevSig - (cmath.cos(alpha)**2*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha))/vev + (cmath.cos(alpha)**2*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha))/vevSig',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '3*complex(0,1)*lam1*cmath.cos(alpha)**3*cmath.sin(alpha) - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)**3*cmath.sin(alpha))/vevSig**2 - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)**3*cmath.sin(alpha))/vevSig**2 + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)**3*cmath.sin(alpha))/vevSig**2',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = 'ee**2*complex(0,1)*cmath.sin(alpha)**2 + (cw**2*ee**2*complex(0,1)*cmath.sin(alpha)**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*cmath.sin(alpha)**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-0.5*(complex(0,1)*lam3*cmath.sin(alpha)**2) - (2*complex(0,1)*METAP**2*cmath.sin(alpha)**2)/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.sin(alpha)**2)/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.sin(alpha)**2)/vevSig**2',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '-0.5*(complex(0,1)*lam3*cmath.sin(alpha)**2) - (2*complex(0,1)*METAI**2*cmath.sin(alpha)**2)/vev**2 + (2*complex(0,1)*METAP**2*cmath.sin(alpha)**2)/vev**2 - (2*complex(0,1)*METAP**2*cmath.sin(alpha)**2)/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.sin(alpha)**2)/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.sin(alpha)**2)/vevSig**2',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '-0.5*(complex(0,1)*lam3*cmath.sin(alpha)**2) + (2*complex(0,1)*METAP**2*cmath.sin(alpha)**2)/vev**2 - (2*complex(0,1)*METAR**2*cmath.sin(alpha)**2)/vev**2 - (2*complex(0,1)*METAP**2*cmath.sin(alpha)**2)/vevSig**2 + (2*complex(0,1)*muEta**2*cmath.sin(alpha)**2)/vevSig**2 + (complex(0,1)*lam3*vev**2*cmath.sin(alpha)**2)/vevSig**2',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((complex(0,1)*Mh1**2*cmath.sin(alpha)**2)/vevSig**2) - (complex(0,1)*Mh2**2*cmath.sin(alpha)**2)/vevSig**2 + (complex(0,1)*lam1*vev**2*cmath.sin(alpha)**2)/vevSig**2 + (cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**2)/(vev*vevSig)',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '-3*complex(0,1)*lam1*vev*cmath.cos(alpha)*cmath.sin(alpha)**2 - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)*cmath.sin(alpha)**2)/vevSig - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)*cmath.sin(alpha)**2)/vevSig + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)*cmath.sin(alpha)**2)/vevSig - (cmath.cos(alpha)*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**2)/vev - (cmath.cos(alpha)*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**2)/vevSig',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-3*complex(0,1)*lam1*cmath.cos(alpha)**2*cmath.sin(alpha)**2 - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)**2*cmath.sin(alpha)**2)/vevSig**2 - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)**2*cmath.sin(alpha)**2)/vevSig**2 + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)**2*cmath.sin(alpha)**2)/vevSig**2 - (2*cmath.cos(alpha)**2*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**2)/(vev*vevSig)',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '3*complex(0,1)*lam1*vev*cmath.sin(alpha)**3 - (3*complex(0,1)*Mh1**2*cmath.sin(alpha)**3)/vevSig - (3*complex(0,1)*Mh2**2*cmath.sin(alpha)**3)/vevSig + (3*complex(0,1)*lam1*vev**2*cmath.sin(alpha)**3)/vevSig + (3*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**3)/vev - (3*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**3)/vevSig',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '3*complex(0,1)*lam1*cmath.cos(alpha)*cmath.sin(alpha)**3 - (3*complex(0,1)*Mh1**2*cmath.cos(alpha)*cmath.sin(alpha)**3)/vevSig**2 - (3*complex(0,1)*Mh2**2*cmath.cos(alpha)*cmath.sin(alpha)**3)/vevSig**2 + (3*complex(0,1)*lam1*vev**2*cmath.cos(alpha)*cmath.sin(alpha)**3)/vevSig**2',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '-3*complex(0,1)*lam1*cmath.sin(alpha)**4 - (3*complex(0,1)*Mh1**2*cmath.sin(alpha)**4)/vevSig**2 - (3*complex(0,1)*Mh2**2*cmath.sin(alpha)**4)/vevSig**2 + (3*complex(0,1)*lam1*vev**2*cmath.sin(alpha)**4)/vevSig**2 + (6*cmath.sqrt(Mh1**2 - lam1*vev**2)*cmath.sqrt(Mh2**2 - lam1*vev**2)*cmath.sin(alpha)**4)/(vev*vevSig)',
                  order = {'QED':2})

