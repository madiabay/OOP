class Personnn:
    def __init__(self, name) -> None:
        self.name = name
        self.__age = 20
    
    # def print_info(self):
    #     print(f'Name: {self.name}, Age: {self.__age}')
    # 
    # def get_age(self):
    #     return self.__age
# 
    # def set_age(self, value):
    #     self.__age = value

    "с помощью декоратора"
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    
    @age.deleter
    def age(self):
        del self.__age
        print('АТРИБУТ УДАЛЕН')