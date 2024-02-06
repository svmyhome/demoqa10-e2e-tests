"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @pytest.mark.parametrize("quantity", [1, 1000])
    def test_product_check_quantity(self, product, quantity):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(quantity), 'incorrect quantity entered'

    @pytest.mark.parametrize("wrong_quantity", [-1, 0, 1001, 'cdscsdc3'])
    def test_product_check_wrong_quantity(self, product, wrong_quantity):
        # TODO напишите проверки на метод check_quantity
        assert not product.check_quantity(wrong_quantity), 'incorrect quantity entered'

    @pytest.mark.parametrize("quantity", [1, 1000])
    def test_product_buy(self, product, quantity):
        # TODO напишите проверки на метод buy
        assert product.buy(quantity) == product.price * quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match='To much quantity'):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
