import math

def add_frac(frac1, frac2):
    sum_of_frac = []
    sum_of_frac = [frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]]
    gcd = math.gcd(sum_of_frac[0], sum_of_frac[1])
    sum_of_frac[0] /= gcd
    sum_of_frac[1] /= gcd
    return sum_of_frac
#Powyżej bez użycia mojej funkcji function_gcd duzo kodu, dlatego napisałem raz zeby nie powtarzać

def sub_frac(frac1, frac2):
    sub_of_frac = [frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]]
    return function_gcd(sub_of_frac)


def mul_frac(frac1, frac2):  # frac1 * frac2
    mul_of_frac = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return function_gcd(mul_of_frac)

def div_frac(frac1, frac2):   # frac1 / frac2
    try:
        assert frac2[0] != 0
        var0 = frac2[0]
        frac2[0] = frac2[1]
        frac2[1] = var0
    # albo to samo w jednej linijce frac2[0], frac2[1] = frac2[1], frac2[0]
    except AssertionError:
        return ZeroDivisionError
    return function_gcd(mul_frac(frac1, frac2))



def is_positive(frac):     # bool, czy dodatni
    if frac2float(frac) > 0:
        return True
    else:
        return False



def is_zero(frac):  # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2): # -1 | 0 | +1
    if frac2float(frac1) == frac2float(frac2):
        return 0
    elif frac2float(frac1) < frac2float(frac2):
        return -1
    else:
        return 1


def function_gcd(frac):
    gcd = math.gcd(frac[0], frac[1])
    if gcd > 1:
        frac[0] /= gcd
        frac[1] /= gcd
    return frac

def frac2float(frac):  # konwersja do float
    return frac[0]/frac[1]