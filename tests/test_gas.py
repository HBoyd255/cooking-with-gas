import unittest

from cooking_with_gas import Gas


class TestGas(unittest.TestCase):

    def test_constructor(self):

        with self.assertRaises(TypeError):
            gas = Gas()

        with self.assertRaises(TypeError):
            gas = Gas(123)

        gas = Gas("DEPLOYMENT_ID")

    def test_get_deployment_id(self):

        gas = Gas("DEPLOYMENT_ID_123")
        self.assertEqual(gas.get_deployment_id(), "DEPLOYMENT_ID_123")

    def test_get_url(self):

        gas = Gas("DEPLOYMENT_ID_123")
        self.assertEqual(
            gas.get_url(),
            "https://script.google.com/macros/s/DEPLOYMENT_ID_123/exec",
        )


if __name__ == "__main__":
    unittest.main()
