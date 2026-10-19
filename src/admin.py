from user import User


class Admin(User):
    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)
        self.id = 0
        self.customers = []