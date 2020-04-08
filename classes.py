class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        return cls(store.name + ' - franchise')  #returns a Store object

    @staticmethod
    def store_details(store):
        print(f'{store.name}, total stock price: {store.stock_price()}')



monop = Store('Monoprix')
monop.add_item('pasta', 1.60)
monop.add_item('rice', 2.40)

print(monop.items)
print(monop.stock_price())

monopf = Store.franchise(monop)
print(monopf.name)
Store.store_details(monop)