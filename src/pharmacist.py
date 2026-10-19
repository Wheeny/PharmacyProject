from user import User


class Pharmacist(User):
    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)
        self.id = 0
