class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def mystaticmethod():
        return 'Static Method'


p1 = Person('Rohit', 38, 'Male')
print(p1.name)
p1.name = 'Rahul'
print(p1.name)
print(Person.mystaticmethod())
print(p1.mystaticmethod())
