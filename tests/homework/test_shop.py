"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.conftest import product, empty_cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @pytest.mark.parametrize("quantity", [1, 1000])
    def test_product_check_correct_quantity(self, product, quantity):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(quantity), 'Incorrect quantity entered'

    @pytest.mark.parametrize("wrong_quantity", [-1, 0, 1001, 'cdscsdc3'])
    def test_product_check_wrong_quantity(self, product, wrong_quantity):
        # TODO напишите проверки на метод check_quantity
        assert not product.check_quantity(wrong_quantity), 'Incorrect quantity entered'

    @pytest.mark.parametrize("quantity", [1, 1000])
    def test_product_buy(self, product, quantity):
        # TODO напишите проверки на метод buy
        total_quantity = product.quantity - quantity
        product.buy(quantity)
        assert product.quantity == total_quantity

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

    def test_add_new_product_with_default_count(self, empty_cart, product):
        default_quantity = 1
        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product)
        assert product in empty_cart.products
        assert (
            empty_cart.products[product] == default_quantity
        ), f'Quantity is not equal to the value {default_quantity}'

    def test_add_new_product(self, empty_cart, product):
        quantity = 5
        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)
        assert product in empty_cart.products
        assert (
            empty_cart.products[product] == quantity
        ), f'Quantity is not equal to the value {quantity}'

    def test_add_same_product(self, empty_cart, product):
        quantity = 5
        total_quantity = 6

        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product)

        empty_cart.add_product(product, quantity)
        assert product in empty_cart.products
        assert (
            empty_cart.products[product] == total_quantity
        ), f'Quantity is not equal to the value {total_quantity}'

    def test_remove_product_less_cart(self, empty_cart, product):
        quantity = 6
        divide = 3

        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)

        empty_cart.remove_product(product, divide)
        assert product in empty_cart.products
        assert (
            empty_cart.products[product] == quantity - divide
        ), f'Quantity is not equal to the value {quantity - divide}'

    @pytest.mark.parametrize("divide", [6, 7])
    def test_remove_product_wrong_count(self, empty_cart, product, divide):
        quantity = 6

        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)

        empty_cart.remove_product(product, divide)
        assert (
            empty_cart.products == {}
        ), f'Quantity is not equal to the value {quantity - divide}'

    def test_remove_product_none(self, empty_cart, product):
        quantity = 6

        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)

        empty_cart.remove_product(product)
        assert (
            empty_cart.products == {}
        ), f'Quantity is not equal to the value {quantity}'

    def test_remove_product_value_error(self, empty_cart, product):
        quantity = 6
        divide = 'wrong value'
        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)
        with pytest.raises(ValueError, match='Wrong quantity'):
            empty_cart.remove_product(product, divide)

    def test_clear_cart(self, empty_cart, product):
        quantity = 6
        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)
        empty_cart.clear()
        assert empty_cart.products == {}, f'Count did not equal {quantity}'

    def test_get_total_price(self, empty_cart, product):
        quantity = 5
        assert empty_cart.products == {}, f'The Cart is not empty'
        empty_cart.add_product(product, quantity)
        assert product in empty_cart.products
        assert (
            empty_cart.products[product] == quantity
        ), f'Quantity is not equal to the value {quantity}'
        assert (
            empty_cart.get_total_price() == product.price * quantity
        ), f'Quantity is not equal to the value {quantity}'

    @pytest.mark.parametrize('quantity', [1, 1000])
    def test_buy(self, empty_cart, product, quantity):
        total_quantity = product.quantity - quantity
        empty_cart.add_product(product, quantity)
        empty_cart.buy()
        assert product.quantity == total_quantity

    def test_buy_more_than_available(self, empty_cart, product):
        empty_cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            empty_cart.buy()
