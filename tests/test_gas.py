import unittest

from cooking_with_gas import Gas


class TestGas(unittest.TestCase):

    def test_constructor(self):

        with self.assertRaises(TypeError):
            gas = Gas()

        with self.assertRaises(TypeError):
            gas = Gas(123)

        gas = Gas("DEPLOYMENT_ID")


if __name__ == "__main__":
    unittest.main()
