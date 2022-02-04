"""

PRODUCTS AND CART

Specyfikacja Cart:
*   Konstruktor nie przyjmuje parametrów. Jest w nim tworzna pusta lista self._products.
*   Metoda get_products() zwraca listę produktów w koszyku
*   Metoda add_product(product) dodaje obiekt class Product do listy produktów (do koszyka)
*   Metada get_products_number() zwaraca liczbę produktów w koszyku
*   Metoda compute_sum() zwaraca sumę cen wszystkich produktów w koszyku

Napisz test oraz zbadaj coverage. Do mockowania uzyj obiektów MagicMock().

"""
from typing import List

from exercises.exercise_7_mocks_products_and_cart.product import Product


class Cart:

    def __init__(self):
        self._products: List[Product] = []

    def get_products(self):
        return self._products

    def add_product(self, product: Product):
        self._products.append(product)

    def get_products_number(self):
        return len(self._products)

    def compute_sum(self):
        product_sum = 0
        for product in self._products:
            product_sum += product.get_price()
        return product_sum
