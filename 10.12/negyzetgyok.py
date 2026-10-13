import math
import unittest

def negyzetgyok(szam: int):
    if szam <0:
        return "A mínusz számokat nem lehet gyökre vonni"
    elif szam == 0:
        return 0
    else:
        return math.sqrt(szam)
    
class test_sqrtFunction(unittest.TestCase):
    def test_sqrts(self):
        teszt = negyzetgyok(4)
        self.assertAlmostEqual(teszt, 2)

    def test_minussqrt(self):
        teszt = negyzetgyok(-3)
        self.assertEqual(teszt, "A mínusz számokat nem lehet gyökre vonni")

    def test_nullsqrt(self):
        teszt = negyzetgyok(0)
        self.assertEqual(teszt, 0)

unittest.main()