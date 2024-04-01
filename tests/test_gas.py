import unittest

from cooking_with_gas import Gas


class TestGas(unittest.TestCase):
    def test_add_one(self):

        # Prints the current File
        print(__file__)

        # Prints the current environment
        print("The name is", __name__)

        gas = Gas()

        result = gas.add_one(1)

        self.assertEqual(result, 2)

        print()


if __name__ == "__main__":
    unittest.main()
