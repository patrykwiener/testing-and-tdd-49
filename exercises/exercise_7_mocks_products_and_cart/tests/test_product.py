import pytest

from exercises.exercise_7_mocks_products_and_cart.product import Product, PriceLessOrEqualZeroError


class TestProduct:
    TEST_NAME = 'test'
    TEST_PRICE = 20

    def setup_method(self) -> None:
        self.product = Product(self.TEST_NAME, self.TEST_PRICE)

    def test_product_get_name(self):
        expected = self.TEST_NAME
        actual = self.product.get_name()
        assert expected == actual

    def test_product_get_price(self):
        expected = self.TEST_PRICE
        actual = self.product.get_price()
        assert expected == actual

    def test_raises_exception_on_less_or_equal_zero(self):
        with pytest.raises(PriceLessOrEqualZeroError):
            Product(self.TEST_NAME, 0)
