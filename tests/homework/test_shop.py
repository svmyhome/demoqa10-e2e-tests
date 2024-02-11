"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

#todo разделить на пустую корзину и корзину с товаром
@pytest.fixture
def empty_cart():
    return Cart()
@pytest.fixture
def one_item_in_cart():
    book = Product("book", 100, "This is a book", 1000)
    cart = Cart()
    cart.add_product(book, 5)
    # eraser = Product("eraser", 2.5, "This is a earaser", 120)
    # cart = Cart()
    # cart.add_product(book)
    # cart.add_product(pen, 10)
    # cart.add_product(eraser, 12)
    return cart


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
        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product)
        assert product in empty_cart.products
        assert empty_cart.products[product] == 1, f'Count not equal 1'

    def test_add_new_product(self, empty_cart, product):
        quantity = 5
        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)
        assert product in empty_cart.products
        assert empty_cart.products[product] == quantity, f'Count not equal {quantity}'

    def test_add_same_product(self, empty_cart, product):
        quantity = 5
        total_quantity = 6

        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product)

        empty_cart.add_product(product, quantity)
        assert product in empty_cart.products
        assert (
                empty_cart.products[product] == total_quantity
        ), f'Count did not equal {total_quantity}'

    def test_remove_product_less_cart(self, empty_cart, product):
        quantity = 6
        divide = 3

        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)

        empty_cart.remove_product(product, divide)
        assert product in empty_cart.products
        assert (
                empty_cart.products[product] == quantity - divide
        ), f'Count did not equal {quantity - divide}'

    @pytest.mark.parametrize("divide", [6, 7])
    def test_remove_product_wrong_count(self, empty_cart, product, divide):
        quantity = 6

        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)

        empty_cart.remove_product(product, divide)
        assert empty_cart.products == {}, f'Count did not equal {quantity - divide}'

    def test_remove_product_none(self, empty_cart, product):
        quantity = 6

        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)

        empty_cart.remove_product(product)
        assert empty_cart.products == {}, f'Count did not equal {quantity}'

    def test_remove_product_value_error(self, empty_cart, product):
        quantity = 6
        divide = 'wrong value'
        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)
        with pytest.raises(ValueError, match='Incorrect count'):
            empty_cart.remove_product(product, divide)

    def test_clear_cart(self, empty_cart, product):
        quantity = 6
        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)
        empty_cart.clear()
        assert empty_cart.products == {}, f'Count did not equal {quantity}'

    def test_get_total_price(self, empty_cart, product):
        quantity = 5
        assert empty_cart.products == {}, f'Cart did not empy'
        empty_cart.add_product(product, quantity)
        assert product in empty_cart.products
        assert empty_cart.products[product] == quantity, f'Count not equal {quantity}'
        assert empty_cart.get_total_price() == product.price * quantity, f'Count not equal {quantity}'

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
