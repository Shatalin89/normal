

class People:
    def __init__(self, lastname, middlename, name, gender, age):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __str__(self):
        return self.name

    def get_age(self):
        return self.age