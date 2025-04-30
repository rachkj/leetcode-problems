class Person:
    def __init__(self, address):
        self.address=address

    def displayAddress(self):
        print(self.address)

class Son(Person):
    def __init__(self,phone,address):

        self.phone=phone
        super().__init__(address)

    def displayPhone(self):
        print(self.phone)

class Grandson(Son):
    def __init__(self,name,phone,address):
        self.name=name
        super().__init__(phone,address)

    def dispayName(self):
        print(self.name)

test=Grandson("Rohan","8577644457","1197 boylston Street")
test.displayAddress()
test.displayPhone()
test.dispayName()
