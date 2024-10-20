import numpy as np
from scipy import optimize


class Z_factor(object):
    def __init__(self):

        self.T = None
        self.sg = None
        self._T = None
        self.P = None
        self.H2S = None
        self.CO2 = None

        self.Tpc = None
        self.Ppc = None
        self.A = None
        self.B = None
        self.e_correction = None
        self.Tpc_corrected = None
        self.Ppc_corrected = None
        self.Pr = None
        self.Tr = None

        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.A4 = None
        self.A5 = None
        self.A6 = None
        self.A7 = None
        self.A8 = None
        self.A9 = None
        self.A10 = None
        self.A11 = None

        self.Z = None

    def __str__(self):
        return str(self.Z)

    def __repr__(self):
        return 'Z_factor(sg=%g, T=%g, P=%g, H2S=%g, CO2=%g), Z=%g' % (
            self.sg, self._T, self.P, self.H2S, self.CO2, self.Z)

    def calc_Fahrenheit_to_Rankine(self, _T):
        if _T is None:
            raise TypeError("Missing a required argument, T (gas temperature, °F)")
        self._T = _T # Fahrenheit
        self.T = T + 459.67 # Rankine, Rankine is used for calculation below
        return self.T

    """pseudo-critical temperature (°R)"""
    def calc_Tpc(self, sg):
        self._initialize_sg(sg)
        self.Tpc = 169.2 + 349.5 * self.sg - 74.0 * self.sg ** 2
        return self.Tpc

    """pseudo-critical pressure (psi)"""
    def calc_Ppc(self, sg):
        self._initialize_sg(sg)
        self.Ppc = 756.8 - 131.07 * self.sg - 3.6 * self.sg ** 2
        return self.Ppc

    """sum of the mole fractions of CO2 and H2S in a gas mixture"""
    def calc_A(self, H2S=0, CO2=0):
        self._initialize_H2S(H2S)
        self._initialize_CO2(CO2)
        self.A = self.H2S + self.CO2
        return self.A

    """mole fraction of H2S in a gas mixture"""
    def calc_B(self, H2S=0):
        self._initialize_H2S(H2S)
        self.B = self.H2S
        return self.B

    """correction for CO2 and H2S (°R)"""
    def calc_e_correction(self, A=None, B=None, H2S=None, CO2=None):
        self._initialize_A(A, H2S=H2S, CO2=CO2)
        self._initialize_B(B, H2S=H2S)
        self.e_correction = 120 * (self.A ** 0.9 - self.A ** 1.6) + 15 * (self.B ** 0.5 - self.B ** 4)
        return self.e_correction

    def calc_Tpc_corrected(self, sg=None, Tpc=None, e_correction=None, A=None, B=None, H2S=None, CO2=None):
        self._initialize_Tpc(Tpc, sg)
        self._initialize_e_correction(e_correction, A, B, H2S, CO2)
        self.Tpc_corrected = self.Tpc - self.e_correction
        return self.Tpc_corrected

    """ corrected pseudo-critical pressure (psi)"""
    def calc_Ppc_corrected(self, sg=None, Tpc=None, Ppc=None, e_correction=None, Tpc_corrected=None,
                           A=None, B=None, H2S=None, CO2=None):
        self._initialize_Ppc(Ppc, sg)
        self._initialize_Tpc(Tpc, sg)
        self._initialize_B(B, H2S=H2S)
        self._initialize_e_correction(e_correction, A, B, H2S=H2S, CO2=CO2)
        self._initialize_Tpc_corrected(Tpc_corrected, sg, Tpc, e_correction, A, B, H2S=0, CO2=0)
        self.Ppc_corrected = (self.Ppc * self.Tpc_corrected) / (self.Tpc - self.B * (1 - self.B) * self.e_correction)
        return self.Ppc_corrected

    """pseudo-reduced temperature (°R)"""
    def calc_Tr(self, T, Tpc_corrected=None, sg=None, Tpc=None, e_correction=None, A=None, B=None, H2S=None, CO2=None):
        self._initialize_T(T)
        self._initialize_Tpc_corrected(Tpc_corrected, sg, Tpc, e_correction, A, B, H2S, CO2)
        self.Tr = self.T / self.Tpc_corrected
        return self.Tr

    """pseudo-reduced pressure (psi)"""
    def calc_Pr(self, P, Ppc_corrected=None, sg=None, Tpc=None, Ppc=None, e_correction=None, Tpc_corrected=None,
                           A=None, B=None, H2S=None, CO2=None):
        self._initialize_P(P)
        self._initialize_Ppc_corrected(Ppc_corrected, sg, Tpc, Ppc, e_correction, Tpc_corrected, A, B, H2S, CO2)
        self.Pr = self.P / self.Ppc_corrected
        return self.Pr

    def _initialize_sg(self, sg):
        if self.sg is None:
            if sg is None:
                raise TypeError("Missing a required argument, sg (specific gravity, dimensionless)")
            else:
                self.sg = sg

    def _initialize_P(self, P):
        if self.P is None:
            if P is None:
                raise TypeError("Missing a required argument, P (gas pressure, psia)")
            else:
                self.P = P

    def _initialize_T(self, T):
        if self.T is None:
            if T is None:
                raise TypeError("Missing a required argument, T (gas temperature, °F)")
            else:
                self.T = self.calc_Fahrenheit_to_Rankine(T)

    def _initialize_H2S(self, H2S):
        self.H2S = H2S

    def _initialize_CO2(self, CO2):
        self.CO2 = CO2

    def _initialize_Tpc(self, Tpc, sg):
        if self.Tpc is None:
            if Tpc is None:
                self._initialize_sg(sg)
                self.calc_Tpc(self.sg)
            else:
                self.Tpc = Tpc

    def _initialize_Ppc(self, Ppc, sg):
        if self.Ppc is None:  # skip calculation is Ppc is already calculated before
            if Ppc is None:
                self._initialize_sg(sg)
                self.calc_Ppc(sg)
            else:
                self.Ppc = Ppc

    def _initialize_e_correction(self, e_correction, A=None, B=None, H2S=None, CO2=None):
        if self.e_correction is None:
            if e_correction is None:
                self.calc_e_correction(A, B, H2S, CO2)
            else:
                self.e_correction = e_correction

    def _initialize_Tpc_corrected(self, Tpc_corrected, sg, Tpc=None, e_correction=None,
                                  A=None, B=None, H2S=None, CO2=None):
        if self.Tpc_corrected is None:
            if Tpc_corrected is None:
                self.calc_Tpc_corrected(sg, Tpc, e_correction, A, B, H2S, CO2)
            else:
                self.calc_Tpc_corrected = Tpc_corrected

    def _initialize_Ppc_corrected(self, Ppc_corrected, sg=None, Tpc=None, Ppc=None, e_correction=None,
                                  Tpc_corrected=None, A=None, B=None, H2S=None, CO2=None):
        if self.Ppc_corrected is None:
            if Ppc_corrected is None:
                self.calc_Ppc_corrected(sg, Tpc, Ppc, e_correction, Tpc_corrected, A, B, H2S, CO2)
            else:
                self.calc_Ppc_corrected = Ppc_corrected

    def _initialize_Pr(self, Pr, P, Ppc_corrected, sg=None, Tpc=None, Ppc=None, e_correction=None, Tpc_corrected=None,
                       A=None, B=None, H2S=None, CO2=None):
        if self.Pr is None:
            if Pr is None:
                self.calc_Pr(P, Ppc_corrected, sg, Tpc, Ppc, e_correction, Tpc_corrected, A, B, H2S, CO2)
            else:
                self.calc_Pr = Pr

    def _initialize_Tr(self, Tr, T, Tpc_corrected, sg, Tpc=None, e_correction=None, A=None, B=None, H2S=None, CO2=None):
        if self.Tr is None:
            if Tr is None:
                self.calc_Tr(T, Tpc_corrected, sg, Tpc, e_correction, A, B, H2S, CO2)
            else:
                self.calc_Tr = Tr

    def _initialize_A(self, A, H2S, CO2):
        if self.A is None:
            if A is None:
                if H2S is None:
                    H2S = 0
                if CO2 is None:
                    CO2 = 0
                self.calc_A(H2S, CO2)
            else:
                self.A = A

    def _initialize_B(self, B, H2S):
        if self.B is None:
            if B is None:
                if H2S is None:
                    H2S = 0
                self.calc_B(H2S)
            else:
                self.B = B

    """Objective function for Newton-Raphson nonlinear solver - Z factor calculation"""
    def _calc_Z(self, z):
        return 1 + (
                self.A1 +
                self.A2 / self.Tr +
                self.A3 / self.Tr ** 3 +
                self.A4 / self.Tr ** 4 +
                self.A5 / self.Tr ** 5
        ) * (0.27 * self.Pr) / (z * self.Tr) + (
                self.A6 +
                self.A7 / self.Tr +
                self.A8 / self.Tr ** 2
        ) * ((0.27 * self.Pr) / (z * self.Tr)) ** 2 - self.A9 * (
                self.A7 / self.Tr +
                self.A8 / self.Tr ** 2
        ) * ((0.27 * self.Pr) / (z * self.Tr)) ** 5 + self.A10 * (
                1 +
                self.A11 * ((0.27 * self.Pr) / (z * self.Tr)) ** 2
        ) * (
                ((0.27 * self.Pr) / (z * self.Tr)) ** 2 /
                self.Tr ** 3
        ) * np.exp(-self.A11 * ((0.27 * self.Pr) / (z * self.Tr)) ** 2) - z

    """Newton-Raphson nonlinear solver"""
    def calc_Z(self, guess=0.9, sg=None, P=None, T=None, Tpc=None, Ppc=None, Tpc_corrected=None, Ppc_corrected=None,
               H2S=0, CO2=0, Tr=None, Pr=None):

        self.A = self.calc_A(H2S, CO2)
        self.B = self.calc_B(H2S)
        self.e_correction = self.calc_e_correction(self.A, self.B)

        if Tr is None:
            if Tpc_corrected is None:
                if Tpc is None:
                    self.Tpc = self.calc_Tpc(sg)
                else:
                    self.Tpc = Tpc
                self.Tpc_corrected = self.calc_Tpc_corrected(self.Tpc, self.e_correction)
            else:
                self.Tpc_corrected = Tpc_corrected
            self._check_missing_T(T)
            self.T = self.calc_Fahrenheit_to_Rankine(self._T)
            self.Tr = self.calc_Tr(self.T, self.Tpc_corrected)
        else:
            self.Tr = Tr

        if Pr is None:
            if Ppc_corrected is None:
                if Ppc is None:
                    self.Ppc = self.calc_Ppc(sg)
                else:
                    self.Ppc = Ppc
                if Tpc is None:
                    self.Tpc = self.calc_Tpc(sg)
                else:
                    self.Tpc = Tpc
                if Tpc_corrected is None:
                    self.Tpc_corrected = self.calc_Tpc_corrected(self.Tpc, self.e_correction)
                else:
                    self.Tpc_corrected = Tpc_corrected
                self.Ppc_corrected = self.calc_Ppc_corrected(self.Ppc, self.Tpc, self.e_correction, self.B,
                                                             self.Tpc_corrected)
            else:
                self.Ppc_corrected = Ppc_corrected
            self._check_missing_P(P)
            self.Pr = self.calc_Pr(self.P, self.Ppc_corrected)
        else:
            self.Pr = Pr

        self.A1 = 0.3265
        self.A2 = -1.0700
        self.A3 = -0.5339
        self.A4 = 0.01569
        self.A5 = -0.05165
        self.A6 = 0.5475
        self.A7 = -0.7361
        self.A8 = 0.1844
        self.A9 = 0.1056
        self.A10 = 0.6134
        self.A11 = 0.7210

        self.Z = optimize.newton(self._calc_Z, guess)
        return self.Z

    def _check_missing_P(self, P):
        if P is None:
            raise TypeError("Missing a required argument, P (gas pressure, psia)")
        self.P = P

    def _check_missing_T(self, _T):
        if _T is None:
            raise TypeError("Missing a required argument, T (gas temperature, °F)")
        self._T = _T



