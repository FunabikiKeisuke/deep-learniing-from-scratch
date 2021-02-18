import unittest
import numpy as np
from chapter03.relu import relu


class ReluTestCase(unittest.TestCase):
    """relu をテストするテストケース"""

    def test_boundary(self):
        expected = 0
        actual = relu(0)
        self.assertEqual(expected, actual)

    def test_representative(self):
        expected = 3.9842938
        actual = relu(3.9842938)
        self.assertEqual(expected, actual)

    def test_infinity(self):
        expected = float('inf')
        actual = relu(float('inf'))
        self.assertEqual(expected, actual)

    def test_supports_ndarray(self):
        expected = np.array([0, 0, 1])
        actual = relu(np.array([-1, 0, 1]))
        np.testing.assert_equal(expected, actual)
