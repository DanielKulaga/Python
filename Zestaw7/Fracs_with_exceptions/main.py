import math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        try:
            assert y != 0
            self.x = x
            self.y = y
            gcdd = math.gcd(self.x, self.y)
            if gcdd > 1:
                self.x /= gcdd
                self.y /= gcdd
            #else:
             #   self.x = 0
             #   self.y = 0
        except AssertionError:
            raise ValueError

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.x == 0:
            return '0/0'
        elif self.y == 1:
            return '{}'.format(self.x)
        return '{}/{}'.format(self.x, self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return 'Frac({}, {})'.format(self.x, self.y)

    # Python 2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        if isinstance(other, float):
            float_as_frac = other.as_integer_ratio()
            if(float_as_frac[0] == self.x and float_as_frac[1] == self.y):
                return True
            else:
                return False
        if isinstance(other, int):
            other.y = 1
            if(self.x == other.x):
                return True
            else:
                return False

        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    # def __gt__(self, other): pass

    # def __ge__(self, other): pass

    def __add__(self, other):  # frac1 + frac2
        if isinstance(other, float):
            float_as_frac = other.as_integer_ratio()
            other = Frac(float_as_frac[0], float_as_frac[1])
            return Frac(int(self.x * other.y + self.y * other.x), int(self.y * other.y))
        elif isinstance(other, int):
            return Frac(self.x + (other * self.y), self.y)
        else:
            return Frac(int(self.x * other.y + self.y * other.x), int(self.y * other.y))
    __radd__ = __add__  # int+frac

    def __sub__(self, other):  # frac1 - frac2
        if isinstance(other, float):
            float_as_frac = other.as_integer_ratio()
            other = Frac(float_as_frac[0], float_as_frac[1])
            return Frac(int(self.x * other.y - self.y * other.x), int(self.y * other.y))
        elif isinstance(other, int):
            return Frac(int(self.x - (other * self.y)), int(self.y))
        else:
            return Frac(int(self.x * other.y - self.y * other.x), int(self.y * other.y))

    def __mul__(self, other):
        if isinstance(other, float):
            float_as_frac = other.as_integer_ratio()
            other = Frac(float_as_frac[0], float_as_frac[1])
        if isinstance(other, int):
            return Frac(int(self.x * other), int(self.y * 1))

        return Frac(int(self.x * other.x), int(self.y * other.y))

    # def __div__(self, other):  # frac1 / frac2, Python 2
    #   other.x, other.y = other.y, other.x
    #   div_of_frac = self.x * other.x, self.y * other.y
    #   return Frac(div_of_frac)

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        if isinstance(other, float):
            float_as_frac = other.as_integer_ratio()
            other = Frac(float_as_frac[0], float_as_frac[1])
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError
            else:
                return Frac(int(self.x), int(self.y * other))
        try:
            assert other.x != 0
            other.x, other.y = other.y, other.x
            div_of_frac_t = self.x * other.x, self.y * other.y
        except AssertionError:
            return ZeroDivisionError
        return Frac(int(self.x * other.x), int(self.y * other.y))

    def __rtruediv__(self, other):  # int/frac, Python 3
        try:
            assert other.x != 0
            other.x, other.y = other.y, other.x
            self.x = self
            self.y = 1
            if isinstance(other, int):
                return Frac(self.y * other, self.x)
        except AssertionError:
            return ZeroDivisionError
        return Frac(int(self.x * other.x), int(1 * other.y))

    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        return self // other

    def __mod__(self, other):  # frac1 % frac2, opcjonalnie
        return Frac(self.x % other.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        if self.x < 0:
            self.x *= -1
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y  # float(frac)

    def __hash__(self):
        return hash(float(self))  # immutable fracs

    # def __functiongcd__(self):
    #   gcd = math.gcd(self.x, self.y)
    #   if gcd > 1:
    #      self.x /= gcd
    #      self.y /= gcd
    #  return self """
