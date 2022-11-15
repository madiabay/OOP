# внизу код для protected то есть одно подчеркивание
"""
from classes_encapsulation import Person

a = Person('Madi')

print(a._age)
# если одно подчеркивание то тогда автор этой программы не хочет чтобы мы изменили значение, на мы можем изменить значение
a._age = 50
print(a._age)

"""

from classes_encapsulation import Person

a = Person('Madi')

a.print_info()
# print(a.__age) # здесь уже выходит ошибка то есть мы не может посмотреть через print атрибут __age
a.__age = 50 # еще не можем изменять значение атрибута
a.print_info()