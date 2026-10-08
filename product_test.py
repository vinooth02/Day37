import unittest
from product import Product


class ProductTest(unittest.TestCase):

    def setUp(self):
        self.product = Product("Laptop", 50000)

    def test_name(self):
        self.assertEqual(self.product.name, "Laptop")

    def test_price(self):
        self.assertEqual(self.product.price, 50000)

    def test_discount(self):
        result = self.product.calculate_discount(10)

        self.assertEqual(result, 45000)


if __name__ == "__main__":
    unittest.main()