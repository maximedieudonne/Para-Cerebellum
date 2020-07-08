"""
here are the labels used by the different software i evaluate writen as dictionary.
"""
label_cnn = {
    0: 'BG',
    12: 'CM',
    33: 'R_I-III',
    36: 'L_I-III',
    43: 'R_IV',
    46: 'L_IV',
    53: 'R_V',
    56: 'L_V',
    60: 'V_VI',
    63: 'R_VI',
    66: 'L_VI',
    70: 'V_VII',
    73: 'R_CRI',
    74: 'R_CRII',
    75: 'R_VIIB',
    76: 'L_CRI',
    77: 'L_CRII',
    78: 'L_VIIB',
    80: 'V_VIII',
    83: 'R_VIIIA',
    84: 'R_VIIIB',
    86: 'L_VIIIA',
    87: 'L_VIIIB',
    90: 'V_IX',
    93: 'R_IX',
    96: 'L_IX',
    100: 'V_X',
    103: 'R_X',
    106: 'L_X'
}
label_suit = {
    0: 'BG',
    1: 'R_I-IV',
    2: 'L_I-IV',
    3: 'R_V',
    4: 'L_V',
    5: 'R_VI',
    6: 'V_VI',
    7: 'L_VI',
    8: 'R_CrusI',
    9: 'V_CrusI',
    10: 'L_CrusI',
    11: 'R_CrusII',
    12: 'V_CrusII',
    13: 'L_CrusII',
    14: 'R_VIIb',
    15: 'V_VIIb',
    16: 'L_VIIb',
    17: 'R_VIIIa',
    18: 'V_VIIIa',
    19: 'L_VIIIa',
    20: 'R_VIIIb',
    21: 'V_VIIIb',
    22: 'L_VIIIb',
    23: 'R_IX',
    24: 'V_IX',
    25: 'L_IX',
    26: 'R_X',
    27: 'V_X',
    28: 'L_X',
    29: 'R_Dentate',
    30: 'L_Dentate',
    31: 'R_Interposed',
    32: 'L_Interposed',
    33: 'R_Fastigial',
    34: 'L_Fastigial'
}

label_suiter = {
    0: 'BG',
    1: 'R_I-IV',
    2: 'L_I-IV',
    3: 'R_V',
    4: 'L_V',
    5: 'R_VI',
    6: 'V_VI',
    7: 'L_VI',
    8: 'R_CrusI',
    9: 'V_CrusI',
    10: 'L_CrusI',
    11: 'R_CrusII',
    12: 'V_CrusII',
    13: 'L_CrusII',
    14: 'R_VIIb',
    15: 'V_VIIb',
    16: 'L_VIIb',
    17: 'R_VIIIa',
    18: 'V_VIIIa',
    19: 'L_VIIIa',
    20: 'R_VIIIb',
    21: 'V_VIIIb',
    22: 'L_VIIIb',
    23: 'R_IX',
    24: 'V_IX',
    25: 'L_IX',
    26: 'R_X',
    27: 'V_X',
    28: 'L_X',
    29: 'R_Dentate',
    30: 'L_Dentate',
    31: 'R_Interposed',
    32: 'L_Interposed',
    33: 'R_Fastigial',
    34: 'L_Fastigial'
}

label_suiter_cnn = {
    'BG': [['BG'], ['BG']],
    'R_I-IV': [['R_I-IV'], ['R_I-III', 'R_IV']],
    'L_I-IV': [['L_I-IV'], ['L_I-III', 'L_IV']],
    'R_V': [['R_V'], ['R_V']],
    'L_V': [['L_V'], ['L_V']],
    'R_VI': [['R_VI'], ['R_VI']],
    'V_VI': [['V_VI'], ['V_VI']],
    'L_VI': [['L_VI'], ['L_VI']],
    'V_VII': [['V_CrusI', 'V_CrusII', 'V_VIIb'], ['V_VII']],
    'R_CrusI': [['R_CrusI'], ['R_CRI']],
    'R_CrusII': [['R_CrusII'], ['R_CRII']],
    'R_VIIB': [['R_VIIb'], ['R_VIIB']],
    'L_CrusI': [['L_CrusI'], ['L_CRI']],
    'L_CrusII': [['L_CrusII'], ['L_CRII']],
    'L_VIIB': [['L_VIIb'], ['L_VIIB']],
    'V_VIII': [['V_VIIIa', 'V_VIIIb'], ['V_VIII']],
    'R_VIIIA': [['R_VIIIa'], ['R_VIIIA']],
    'R_VIIIB': [['R_VIIIb'], ['R_VIIIB']],
    'L_VIIIA': [['L_VIIIa'], ['L_VIIIA']],
    'L_VIIIB': [['L_VIIIb'], ['L_VIIIB']],
    'V_IX': [['V_IX'], ['V_IX']],
    'R_IX': [['R_IX'], ['R_IX']],
    'L_IX': [['L_IX'], ['L_IX']],
    'V_X': [['V_X'], ['V_X']],
    'R_X': [['R_X'], ['R_X']],
    'L_X': [['L_X'], ['L_X']]
}
