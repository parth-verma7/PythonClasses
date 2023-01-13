import math
from typing import List

class Complex:
    def __init__( self, real, imaginary ):
        self.real = real
        self.imaginary = imaginary

    def __eq__( self , other ):
        if not isinstance( other, Complex ):

            return NotImplemented

        return ( self.real , self.imaginary ) == ( other.real, other.imaginary )

    def __repr__(self):

        return f"Complex(real={self.real} , imaginary={self.imaginary})"

    def __str__(self):
        if(self.imaginary<0): sign='-'
        else: sign='+'

        return f"{self.real} {sign} {abs(self.imaginary)}i"

    def __abs__(self):

        return math.sqrt(self.real**2 +self.imaginary**2)

    def __add__(self, other):

        if not isinstance(other, Complex):
            return NotImplemented

        return Complex( self.real + other.real, self.imaginary +other.imaginary )

    def __iadd__( self, other ):

        if not isinstance( other, Complex ):
            return NotImplemented

        self.real += other.real
        self.imaginary += other.imaginary

        return self

    @staticmethod
    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
        real_sum = comp.real
        imag_sum = comp.imaginary

        for co in comps:
            real_sum += co.real
            imag_sum += co.imaginary
        return Complex(real_sum, imag_sum)

c1 = Complex(-1, -2)
c2 = Complex(2, 4)
c3 = Complex(1, 2)
print(c1 == c3, c1 + c2 == c3)
print(repr(c1))
print(c1)
print(abs(c1))
print(c1 + c2)
c1 += c3
print(c1)
print(Complex.add_all(c2, c2, c3))
try:
    c1 + 1
except TypeError as e:
    print(f"{type(e).__name__}: {e}")