
from abc import abstractmethod, ABC
import matplotlib.pyplot as plt
'''
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

'''


class WithMessage(object):
    def __init__(self, message) -> None:
        self.message = message

    def __enter__(self):
        print(f"entering with message {self.message}")
        return self.message
    
    def __exit__(self, *args):
        print("Exit with message")

    
with WithMessage("Hello") as msg:
    print(msg)



class Vector:
    '''
    h detta är en klass som representerar euclidean vectors h 
    e detta är en klass som representerar euclidean vectors e
    j detta är en klass som representerar euclidean vectors j
    s detta är en klass som representerar euclidean vectors s
    a detta är en klass som representerar euclidean vectors a
    n detta är en klass som representerar euclidean vectors n
    '''
    def __init__(self, *numbers) -> None:
        # error checking
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} is not a valid number")
        if len(numbers) <= 0:
            raise ValueError("Vector can't be empty")
        
        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self):
        return self._numbers
    
    @staticmethod
    def validate2d(instance):
        return len(instance) == 2
    


    def __add__(self,other):
        if self.validate_vector(other):
            numbers = (a+b for a, b in zip(self._numbers, other.numbers))
            return Vector(*numbers)
        else:
            pass

    def __sub__(self,other):
        if self.validate_vector(other):
            numbers = (a-b for a, b in zip(self._numbers, other.numbers))
            return Vector(*numbers)
        else:
            pass

    def __mul__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Value must be a scalar(int or float).")
        numbers = (value*a for a in self.numbers)
        return Vector(*numbers)
    
    def __rmul__(self,value):
        return self*value

    def __len__(self):
        return len(self.numbers)

    def validate_vector(self, other):
        if not isinstance (other, Vector) or (len(self)!= len(other)):
            raise ValueError(f"{other} is not a vector")    
        return True
    
    def __abs__(self):
        '''
        returns the Euclidean norm of a vector, aka the L2-norm
        '''
        return sum(a**2 for a in self.numbers) ** .5

    def __getitem__(self,idx):
        return self.numbers[idx]

    def __repr__(self):
        return f"Vector{self.numbers}"
    
    @staticmethod
    def plot(*vectors):
        x, y = [], []
        
        for v in tuple(vectors):
            if Vector.validate2d(v):
                x.append(v[0])
                y.append(v[1])
        
        originX = originY = tuple(0 for _ in range(len(x)))
        plt.quiver(originX, originY, x, y, angles="xy", scale_units="xy", scale = 1)
        plt.xlim(-2,10)
        plt.ylim(-2,10)
        plt.grid()
        plt.show()

    
v = Vector(2,4)
u = Vector(4,6)
print(u+v)
print(u-v)
print(3*u)
print(abs(v))
print(u[1])
print(Vector.validate2d(v))

Vector.plot()