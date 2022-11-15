# внизу код класса для protected то есть одно подчеркивание
"""
class Person:
    def __init__(self, name) -> None:
        self.name = name
        self._age = 20
    
    def print_info(self):
        print(f'Name: {self.name}, Age: {self._age}')

"""

# внизу для private то есть 2 подчеркивание
class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.__age = 20
    
    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')