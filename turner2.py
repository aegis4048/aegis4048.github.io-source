import numpy as np
from scipy import optimize


class Z_factor(object):
    def __init__(self,
                 sg=None,
                 T=None,
                 P=None,
                 H2S=0.0,
                 CO2=0.0,
                 Tpc=None,
                 Ppc=None,
                 e_correction=None,
                 Tpc_corrected=None,
                 Ppc_corrected=None,
                 Pr=None,
                 Tr=None,
                 ):

        self.sg = sg             # Specific gravity of gas (dimensionless)
        self._T = T              # Temperature (°R)
        self.P = P               # Pressure (psia)
        self.H2S = H2S           # Mole fraction of H2S (dimensionless)
        self.CO2 = CO2           # Mole fraction of CO2 (dimensionless)

        self.T = self.Fahrenheit_to_Rankine()

        self.A = self.H2S + self.CO2
        self.B = self.H2S

        self.Tpc = Tpc
        self.Ppc = Tpc
        self.e_correction = e_correction
        self.Tpc_corrected = Tpc_corrected
        self.Ppc_corrected = Ppc_corrected
        self.Pr = Pr
        self.Tr = Tr

        if Tpc is None:
            self.Tpc = self.calc_Tpc()
        if Ppc is None:
            self.Ppc = self.calc_Ppc()
        if e_correction is None:
            self.e_correction = self.calc_e_correction()
        if Tpc_corrected is None:
            self.Tpc_corrected = self.calc_Tpc_corrected()
        if Ppc_corrected is None:
            self.Ppc_corrected = self.calc_Ppc_corrected()
        if Pr is None:
            self.Pr = self.calc_Pr()
        if Tr is None:
            self.Tr = self.calc_Tr()

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

        self.Z = self.calc_Z()

    def __str__(self):
        return str(self.Z)

    def __repr__(self):
        return 'Z_factor(sg=%g, T=%g, P=%g, H2S=%g, CO2=%g), Z=%g' % (self.sg, self._T, self.P, self.H2S, self.CO2, self.Z)

    def Fahrenheit_to_Rankine(self):
        return self._T + 459.67

    """pseudo-critical pressure (psi)"""
    def calc_Ppc(self):
        return 756.8 - 131.07 * self.sg - 3.6 * self.sg ** 2

    """pseudo-critical temperature (°R)"""
    def calc_Tpc(self):
        return 169.2 + 349.5 * self.sg - 74.0 * self.sg ** 2

    """correction for CO2 and H2S (°R)"""
    def calc_e_correction(self):
        return 120 * (self.A ** 0.9 - self.A ** 1.6) + 15 * (self.B ** 0.5 - self.B ** 4)

    """corrected pseudo-critical temperature (°R)"""
    def calc_Tpc_corrected(self):
        return self.Tpc - self.e_correction

    """ corrected pseudo-critical pressure (psi)"""
    def calc_Ppc_corrected(self):
        return (self.Ppc * self.Tpc_corrected) / (self.Tpc - self.B * (1 - self.B) * self.e_correction)

    """pseudo-reduced pressure (psi)"""
    def calc_Pr(self):
        return self.P / self.Ppc_corrected

    """pseudo-reduced temperature (°R)"""
    def calc_Tr(self):
        return self.T / self.Tpc_corrected

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
    def calc_Z(self, guess=0.9, sg=None, P=none, T=None, Tpc=None, Ppc=None, Tpc_corrected=None, Ppc_corrected=None,
               H2S=None, CO2=None, Tr=None, Pr=None):

        if T is None:
            self.T = self.Fahrenheit_to_Rankine()

        if Tpc is None:
            self.sg = sg
            self.Tpc = 169.2 + 349.5 * sg - 74.0 * sg ** 2

        if Ppc is None:
            self.sg = sg
            self.Tpc = 169.2 + 349.5 * sg - 74.0 * sg ** 2

        if Tr is None:
            if Tpc is None:
                if sg is None:
                    raise TypeError("Missing a required argument, sg (specific gravity, dimensionless)")
                if T is None:
                    raise TypeError("Missing a required argument, T (temperature, °R)")
                self.Tpc = self.calc_Tpc

            if H2S is None and CO2 is None:
                self.Tpc_corrected = self.Tpc
                self.e_correction = 0
                self.Tr = self.T / self.Tpc
            else:


                self.Tr = self.T / self.Tpc_corrected



        return optimize.newton(self._calc_Z, guess)


a = Z_factor(sg=0.7, T=75, P=2010, H2S=0.07, CO2=0.1)