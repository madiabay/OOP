"""
class Personnn:
    def __init__(self, name) -> None:
        self.name = name
        self.__age = 20
    
    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')
    
    def get_age(self):
        return self.__age
"""

# from classes import Personnn
# 
# a = Personnn('Madi')
# print(a.get_age())

"""
class Personnn:
    def __init__(self, name) -> None:
        self.name = name
        self.__age = 20
    
    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')
    
    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value
"""

# from classes import Personnn
# 
# b = Personnn('Adilet')
# print(b.get_age())
# b.set_age(400)
# print(b.get_age())

"c помошью декоратора getter and setter"
"""

"""

from classes import Personnn
c = Personnn('Kayrat')
print(c.age) # GETTER
c.age = 100 # SETTER
print(c.age) # return new attribute

del c.age # удалили атрибут

print(c.age) # вот здесь мы хотим вывести атрибут age с помощью GETTER, НО не выводится потому что мы удалили атрибут