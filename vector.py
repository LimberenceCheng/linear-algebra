import math
NumberTypes = (int, float, complex)
class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        assert self.dimension == other.dimension
        return Vector([i+j for i,j in zip(self.coordinates, other.coordinates)])
    def __sub__(self, other):
        assert self.dimension == other.dimension
        return Vector([i-j for i,j in zip(self.coordinates, other.coordinates)])
    def __mul__(self, other):
        assert isinstance(other, NumberTypes)
        return Vector([i*other for i in self.coordinates])
    def __rmul__(self, other):
        assert isinstance(other, NumberTypes)
        return Vector([i*other for i in self.coordinates])
    def magitude(self):
        return math.sqrt(sum(i**2 for i in self.coordinates))
    def direction(self):
        l = self.magitude()
        return Vector([i/l for i in self.coordinates])
    def dotProduct(self, other):
        assert isinstance(other, Vector)
        assert self.dimension == other.dimension
        return sum([i*j for i,j in zip(self.coordinates, other.coordinates)])

    def direction_between(self, other):
        return math.acos(self.dotProduct(other)/(self.magitude()*other.magitude()))

    def parallel(self, other,tolerance=1e-10):
        assert isinstance(other, Vector)
        assert self.dimension == other.dimension
        bt = self.direction_between(other)
        negbt = abs(math.pi - bt)
        if bt < tolerance or negbt < tolerance:
            return True
        else:
            return False

    def isOrthogonal(self,v,tolerance=1e-10):
        if abs(self.dotProduct(v)) < tolerance:
            return True
        else:
            return False
    def prejection(self, other):
        return self.dotProduct(other)*other.direction()

myvector = Vector([1,0])
myvector2 = Vector([0,-4])
print(myvector.prejection(myvector2))
