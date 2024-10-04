from abc import abstractmethod, ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side) -> None:
        self._side = side

    @property
    def side(self):
        return self.side
    
    @property
    def area(self):
        return self._side**2


class Rectangle(Shape):
    def __init__(self, long, short) -> None:
        self._long = long
        self._short = short

    @property
    def area(self):
        return self._long * self._short
    


s=Square(2)
r=Rectangle(2,4)


class Person:

    def __init__(self, name) -> None:
        self._name = name
        

class Student(Person):
    
    @property
    def is_studying(self):
        print(f"{self._name} is studying")
        return True
    
class Unemployed(Person):
    
    @property
    def is_studying(self):
        print(f"{self._name} is studying")
        return False
    def is_working(self):
        print(f"{self._name} is not employed")
        return False
    
u = Unemployed("Ada")
s = Student("Einstein")
p = Person("Church")

print(s._name, u._name, p._name)