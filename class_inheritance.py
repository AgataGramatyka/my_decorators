class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} ({self.connected_by})'  # !r calls the repr method of self.name

    def disconnect(self):
        self.connected = False
        print('Disconnected.')


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining)'

    def print(self, pages):
        if not self.connected:
            print('Your printer is not connected!')
            return
        print(f'Printing {pages} pages.')
        self.remaining_pages -= pages

hp = Printer('HP', 'USB', 500)
hp.print(20)
hp.disconnect()
print(hp)