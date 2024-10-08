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
        if not isinstance (other, Vector):
            raise ValueError(f"{other} is not a vector")    
        if (len(self)!= len(other)):
            raise TypeError(f"Dimensions of vector not equal {len(other)} != {len(self)}")
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

    def __eq__(self, other):
        if not self.validate_vector(other):
            False
        
        for v1,v2 in zip(self.numbers, other.numbers):
            if v1 != v2:
                return False

        return True    

if __name__ == '__main__':
    v = Vector(2,4)
    u = Vector(4,6)
    print(u+v)
    print(u-v)
    print(3*u)
    print(abs(v))
    print(u[1])
    print(Vector.validate2d(v))

    Vector.plot()