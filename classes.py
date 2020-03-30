class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, name):
        print(cls(name + '- franchise'))

    @staticmethod
    def store_details(store):
        return f'{store}, total stock price: {store.stock_price()}'



monop = Store('Monoprix')
monop.add_item('pasta', 1.60)
monop.add_item('rice', 2.40)

print(monop.items)
print(monop.stock_price())

Store.franchise('monop')