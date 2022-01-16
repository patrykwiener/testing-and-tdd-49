"""
PRODUCTS AND CART

Naszym zadaniem jest stworzyc imitację koszyka w sklepie internetowym (oczywiście w dużym uproszczeniu). Serwis składa
się z dwóch klas: Product oraz Cart.

Specyfikacja Product:
*   Konstruktor przymuje dwa parametry: name: str, price: float. Są one przechowywane w atrybutach self._name oraz
    self._price.
*   W konstruktorze sprawdzane jest czy cena produktu nie jest mniejsza lub równa zero. W takim przypadku rzucany jest
    wyjątek PriceLessOrEqualZeroError.
*   Metoda get_name() zwraca nazwę produktu.
*   Metoda get_price() zwraca cenę produktu.

Napisz test w pliku tests/test_product.py oraz zbadaj coverage.
"""


class PriceLessOrEqualZeroError(Exception):
    pass


class Product:
    pass
