import unittest
from chapter04.gradient_1d import numerical_diff


class NumericalDiffTestCase(unittest.TestCase):
    """numerical_diff をテストするテストケース"""

    def test_representative(self):
        def _function_1(x):
            return 0.01 * x ** 2 + 0.1 * x

        expected = 0.2
        actual = numerical_diff(_function_1, 5)
        self.assertAlmostEqual(expected, actual, places=11)
