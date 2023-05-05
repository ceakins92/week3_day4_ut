import unittest
from shopping_cart import cart


class Testcart(unittest.TestCase):
    # def test_input_check(self):
    #    self.assertIsInstance(cart.input_check_int(self, input_msg=9), int)

    # def test_instantiation(self):
    #    self.assertIsInstance(cart({'beer': 5.00, 'wine': 7.00}), object)

    def test_remove(self):
        carts = cart()
        carts.grocery_dict = {'apples': {'price': 2, 'quantity': 5}}
        carts.remove()
        self.assertEqual(carts.grocery_dict, {
                         'apples': {'price': 2, 'quantity': 3}})


if __name__ == '__main__':
    unittest.main()
