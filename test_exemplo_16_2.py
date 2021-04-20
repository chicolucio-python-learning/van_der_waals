from exemplo_16_2 import van_der_waals
import numpy as np


def test_valores_exemplo():
    assert np.isclose(van_der_waals(5.5088, 0.065144, 300, 200), 0.096, atol=0.001)
