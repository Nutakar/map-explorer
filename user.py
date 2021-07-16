class User:
    def __init__(self, name, surname, phone, password, pets=[]):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.__password = password
        self.pets = pets

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.phone}, {self.pets}'

    @property
    def password(self, password):
        return self.password

    @password.setter
    def password(self, password):
        self.__password = password

    @password.getter
    def password(self):
        return self.__password

    
class Pet:
    def __init__(self, name, breed, year, master=None):
        self.name = name
        self.breed = breed
        self.year = year
        self.master = master


owner = User('Anna', 'Karpunicheva', '89152330615', 'zaq1xsw2')
cat = Pet('Patric', 'home', 2012)
owner.pets.append(cat)
cat.master = owner
owner.password = 'vfr4'
# password = owner.password
# print(password)
print(owner.password)