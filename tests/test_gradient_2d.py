import unittest
import numpy as np
from chapter04.gradient_2d import numerical_gradient


class NumericalGradientTestCase(unittest.TestCase):
    """numerical_gradient をテストするテストケース"""

    def test_representative(self):
        def _function_1(x):
            if x.ndim == 1:
                return np.sum(x ** 2)
            else:
                return np.sum(x ** 2, axis=1)

        x0 = np.arange(-1, 0, 0.5)
        x1 = np.arange(-1, 0, 0.5)
        X, Y = np.meshgrid(x0, x1)

        X = X.flatten()
        Y = Y.flatten()

        expected = np.array([[-2.0, -1.0, -2.0, -1.0],
                             [-2.0, -2.0, -1.0, -1.0]])
        actual = numerical_gradient(_function_1, np.array([X, Y]).T).T
        np.testing.assert_almost_equal(expected, actual, decimal=11)
