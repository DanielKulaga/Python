# Kod testujący moduł.

import unittest
from times import *
class TestTime(unittest.TestCase):

    def setUp(self):
        self.time1 = "02:04:56"
        self.time2 = "01:50:50"
        self.time3 = "00:00:00"
        self.time4 = "11:11:11"
        self.time5 = "00:59:59"

    def test_print(self):
        # test str()
        self.assertEqual(self.time1, str(Time(7496)))
        self.assertEqual(self.time2, str(Time(6650)))
        self.assertEqual(self.time3, str(Time(0)))
        self.assertEqual(self.time4, str(Time(40271)))
        self.assertEqual(self.time5, str(Time(3599)))

        # test repr()
        self.assertEqual('Time(3599)', repr(Time(3599)))
        self.assertEqual('Time(1293019)', repr(Time(1293019)))
        self.assertEqual('Time(0)', repr(Time(0)))
        self.assertEqual('Time(9999999)', repr(Time(9999999)))
        self.assertEqual('Time(100000000000000)', repr(Time(100000000000000)))

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(6) == Time(3))
        self.assertTrue(Time(98888) != Time(98850))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(16) < Time(100))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(100000000000000000) <= Time(9))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))
        self.assertTrue(Time(100) <= Time(3000))
        self.assertFalse(Time(900) <= Time(899))
        self.assertTrue(Time(12) > Time(5))
        self.assertFalse(Time(10) > Time(100))
        self.assertTrue(Time(456) >= Time(356))
        self.assertTrue(Time(5) >= Time(5))
        self.assertTrue(Time(00000) == Time(0))

    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(10) + Time(20), Time(30))
        self.assertEqual(Time(899) + Time(2), Time(901))
        self.assertEqual(Time(11) + Time(0), Time(11))
        self.assertEqual(Time(10) + Time(0), Time(10))
        self.assertEqual(Time(8) + Time(2), Time(10))
        self.assertEqual(Time(10000) + Time(1000), Time(11000))
        self.assertEqual(Time(999999) + Time(2), Time(1000001))
        self.assertEqual(Time(1) + Time(-2), Time(-1))
        self.assertEqual(Time(100) + Time(999), Time(1099))
        self.assertEqual(Time(-2) + Time(-2), Time(-4))
        self.assertEqual(Time(11119999) + Time(0), Time(11119999))
        self.assertEqual(Time(8) + Time(-8), Time(0))
        self.assertEqual(Time(00000000) + Time(0000000000), Time(0))
        self.assertEqual(Time(8002) + Time(2), Time(8004))
        self.assertEqual(Time(000000000) + Time(-2), Time(-2))
        self.assertEqual(Time(10) + Time(2), Time(12))
        self.assertEqual(Time(8000000000000) + Time(00), Time(8000000000000))
        self.assertEqual(Time(10) + Time(-20), Time(-10))


    def test_int(self):
        self.assertEqual(int(Time(-20)), -20)
        self.assertEqual(int(Time(100)), 100)
        self.assertEqual(int(Time(0)), 0)
        self.assertEqual(int(Time()), 0)
        self.assertEqual(int(Time(568777)), 568777)
        self.assertEqual(int(Time(00000000000)), 0)
        self.assertEqual(int(Time(999999)), 999999)
        self.assertEqual(int(Time(-00000000)), 0)
        self.assertEqual(int(Time(11111)), 11111)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy



