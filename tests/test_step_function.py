import unittest
import numpy as np
from chapter03.step_function import step_function


class StepFunctionTestCase(unittest.TestCase):
    """step_function をテストするテストケース"""

    def test_boundary_return_zero(self):
        expected = 0
        actual = step_function(0)
        self.assertEqual(expected, actual)

    def test_representative(self):
        expected = 0
        actual = step_function(-2)
        self.assertEqual(expected, actual)

        expected = 1
        actual = step_function(4)
        self.assertEqual(expected, actual)

    def test_supports_ndarray(self):
        expected = np.array([0, 0, 1])
        actual = step_function(np.array([-1, 0, 1]))
        np.testing.assert_allclose(expected, actual, rtol=0, atol=0)
