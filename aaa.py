A1 = 0.3265
A2 = -1.0700
A3 = -0.5339
A4 = 0.01569
A5 = -0.05165
A6 = 0.5475
A7 = -0.7361
A8 = 0.1844
A9 = 0.1056
A10 = 0.6134
A11 = 0.7210

Tr=1.5005661019949397
Pr=3.1995450990234966

import numpy as np
from scipy import optimize

def calc_Z(z):
    return 1 + (
            A1 +
            A2 / Tr +
            A3 / Tr ** 3 +
            A4 / Tr ** 4 +
            A5 / Tr ** 5
    ) * (0.27 * Pr) / (z * Tr) + (
            A6 +
            A7 / Tr +
            A8 / Tr ** 2
    ) * ((0.27 * Pr) / (z * Tr)) ** 2 - A9 * (
            A7 / Tr +
            A8 / Tr ** 2
    ) * ((0.27 * Pr) / (z * Tr)) ** 5 + A10 * (
            1 +
            A11 * ((0.27 * Pr) / (z * Tr)) ** 2
    ) * (
            ((0.27 * Pr) / (z * Tr)) ** 2 /
            Tr ** 3
    ) * np.exp(-A11 * ((0.27 * Pr) / (z * Tr)) ** 2) - z

optimize.newton(calc_Z, 0.9)