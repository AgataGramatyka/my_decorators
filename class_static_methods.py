class ClassTest:
    def instance_method(self):
        print(f'called instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f'called class_method of {cls}')

    @staticmethod
    def static_method():
        print("Called static_method.")


class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


hard = Book.hardcover('Harry Potter', 1500)
light = Book.paperback('Python 101', 600)

print(hard)
print(light)

