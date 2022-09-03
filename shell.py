from quickstart.serializers import ItemSerializer


class Item:
    def __init__(self, name, price, qr):
        self.name = name
        self.price = price
        self.qr = qr


items = Item(name="Asus Gaming PC", price=650, qr="1C650P1I")
items_1 = Item(name="Acer Gaming", price=750, qr= "1C750P2I")
items_2 = Item(name="Lenovo Y80", price=550, qr="2C550P3I")
items_3 = Item(name="Xiaomi Redmi Note 10", price=350, qr="3C350P4I")

