class UsersClass:
    name: str
    age: int
    status: str
    items: list[str]

    def __init__(self, name, age, status, items):
        self.name = name
        self.age = age
        self.status = status
        self.items = items

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.age == other.age
            and self.status == other.status
            and self.items == other.items
        )

    def __repr__(self):
        return f'This is rewrite function'


if __name__ == '__main__':
    user1 = UsersClass('Vladimir', 23, 'student', ['book', 'pen'])
    user2 = UsersClass('Vladimir', 23, 'student', ['book', 'pen'])

    print(user1)
    print(user1.__dict__)
