class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if isinstance(quantity, int) and quantity > 0:
            return self.quantity >= quantity
        else:
            return False
    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            return quantity * self.price
        raise ValueError('To much quantity')

    def __hash__(self):
        return hash(self.name + self.description)

    def __repr__(self):
        return f'{self.name}'


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        p1 = product
        if True:
            self.products[product] = buy_count
            print(self.products)
            return self.products
        else:
            raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def get_total_price(self) -> float:
        raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError


if __name__ == '__main__':
    c1 = Cart()
    print(c1.__dict__)
    book = Product("book", 100, "This is a book", 1000)
    book1 = Product("book", 100, "This is a book", 1000)
    products1 = {}

    print(products1)
    products1["cdscsd"] = 1
    products1["cdscsd1"] = 2
    products1[book] = 2
    products1[book1] = 1
    print(products1)
    # products1.
    print(hash(book) == hash(book1))
    print(book == book1)
    print()