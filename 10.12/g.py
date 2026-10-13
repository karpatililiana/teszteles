import unittest
def sajat_abs(szam1: int):
    if szam1 < 0:
        return -szam1
    else:
        return szam1

#hibas_abs(1134)

class TestAbsFunction(unittest.TestCase):
    def test_one_negative(self):
        ertek = sajat_abs(-5)
        self.assertEqual(ertek, 5)

    def test_one_positive(self):
        ertek = sajat_abs(5)
        self.assertGreater(ertek, 0)

    def test_zero(self):
        ertek = sajat_abs(0)
        self.assertEqual(ertek, 0)

unittest.main()
    
