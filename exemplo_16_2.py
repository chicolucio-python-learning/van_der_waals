import numpy as np


GAS_CONSTANT = 0.082057366080960


def van_der_waals(a, b, temperatura, pressao):
    coef_V3 = 1
    coef_V2 = -(b + GAS_CONSTANT * temperatura / pressao)
    coef_V1 = a / pressao
    coef_V0 = - a * b / pressao
    poly = np.polynomial.Polynomial((coef_V0, coef_V1, coef_V2, coef_V3))
    raiz = poly.roots()

    return raiz[np.isreal(raiz)]
