from user import User


class Customer(User):
    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)
        self.cost = 0
        self.cart = []