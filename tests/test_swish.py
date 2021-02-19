import unittest
import numpy as np
from chapter03.swish import swish


class SwishTestCase(unittest.TestCase):
    """swish をテストするテストケース"""

    def test_representative(self):
        expected = 2.85772
        actual = swish(3)
        places = len(str(expected).split('.')[1])
        self.assertAlmostEqual(expected, actual, places=places)

    def test_infinity(self):
        expected = float('inf')
        actual = swish(float('inf'))
        self.assertEqual(expected, actual)

        expected = 0
        actual = swish(-float('inf'))
        self.assertEqual(expected, actual)

    def test_supports_ndarray(self):
        expected = np.array([-0.268941, 0., 0.731059])
        actual = swish(np.array([-1, 0, 1]))
        np.testing.assert_allclose(expected, actual, atol=1e-6)
