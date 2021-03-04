import unittest
from chapter03.neural_mnist import neural_mnist


class NeuralMnistTestCase(unittest.TestCase):
    """neural_mnist をテストするテストケース"""

    def test_representative(self):
        expected = 0.9352
        actual = neural_mnist("chapter03/sample_weight.pkl")
        self.assertEqual(expected, actual)
