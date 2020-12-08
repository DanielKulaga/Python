import random
import math
import unittest

def solve1(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "Równanie ma nieskończenie wiele rozwiązań"
    if a == 0 and b == 0:
        return "Równanie jest sprzeczne"
    elif a == 0:
        result = (-c/b)
        return "Rozwiązanie: y = " + str(result)
    elif b == 0:
        return "Rozwiązanie: x = " + str(-c/a)
    else:
        return "Rozwiązanie : = -({} * x + {}) / {}".format(a, b, c)

#Zad 8.3
def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    num_of_points = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            num_of_points += 1
    return (4 * num_of_points / n)

#Zad 8.4
def heron(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Trójkąt może składać sie tylko z odcinków o dodatniej dlugosci")
    temp = (a + b + c) / 2
    area = math.sqrt(temp * (temp - a) * (temp - b) * (temp - c))
    if isinstance(area, complex):
        raise ValueError
    else:
        return area

#Zad 8.6
def P_recursive(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif j == 0:
        return 0.0
    elif i == 0:
        return 1.0
    else:
        return 0.5 * (P_recursive(i-1, j) + P_recursive(i, j-1))

def P_dynamic(i, j):
    values_P = {}
    if i < 0 and j < 0:
        raise ValueError("Podaj liczby nieujemne")
    values_P[(0, 0)] = 0.5

    for l in range(1, i + 1):
        values_P[(l, 0)] = 0

    for m in range(1, j + 1):
        values_P[(0, m)] = 1.0

    for x in range(1, i + 1):
        for y in range(1, j + 1):
            values_P[(x, y)] = 0.5 * (values_P[(x - 1, y)] + values_P[(x, y - 1)])

    return values_P.get((i, j))

class MyTestCase(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(solve1(0, 0, 0), "Równanie ma nieskończenie wiele rozwiązań")
        self.assertEqual(solve1(0, 0, 3), "Równanie jest sprzeczne")
        self.assertEqual(solve1(0, 2, 3), "Rozwiązanie: y = -1.5")
        self.assertEqual(solve1(3, 4, 5), "Rozwiązanie : = -(3 * x + 4) / 5")

    def test_heron(self):
        try:
            heron(-9, 0, -1)
        except Exception as error1:
            self.assertEqual(error1.__class__, ValueError)
        self.assertEqual(heron(3, 4, 5), 6)
        try:
            heron(0, 0, 0)
        except Exception as error2:
            self.assertEqual(error2.__class__, ValueError)

#Zakładam, że przy 1 000 000 iteracji wynik bedzie zbliżony
    def test_calc_pi(self):
        self.assertAlmostEqual(calc_pi(1000000), math.pi, places=2)
        self.assertAlmostEqual(calc_pi(100000), math.pi, places=1)
        #self.assertAlmostEqual(calc_pi(10000), math.pi, places=2) #za mała dokładność

    def test_P_recursive(self):
        self.assertEqual(P_recursive(1, 2), 0.75)
        self.assertEqual(P_recursive(2, 1), 0.25)
        self.assertEqual(P_recursive(0, 0), 0.5)

    def test_P_dynamic(self):
        try:
            P_dynamic(-9, -1)
        except Exception as error3:
            self.assertEqual(error3.__class__, ValueError)
        self.assertEqual(P_dynamic(1, 2), 0.75)
        self.assertEqual(P_dynamic(2, 3), 0.6875)

if __name__ == '__main__':
    unittest.main()
