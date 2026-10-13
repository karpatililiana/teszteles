import unittest
#gyakorlatijegy
def gyakorlatijegy(ertek: int):
    if  ertek > 100 or ertek < 0:
        jegy = "Érvénytelen érték"
    else:
        if ertek > 85:
            jegy = "Jeles"
        elif ertek > 70:
            jegy = "Jó"
        elif ertek > 55:
            jegy = "Közepes"
        elif ertek > 40:
            jegy = "Elégséges"
        else:
            jegy = "Elégtelen"
    return jegy

class TestJegyFunction(unittest.TestCase):
    def test_szazegy(self):
        teszt = gyakorlatijegy(102)
        self.assertGreater(teszt, 101)

    def test_jeles(self):
        teszt = gyakorlatijegy(100)
        self.assertGreaterEqual(teszt, "Jeles")
    def test_jeles_also(self):
        teszt = gyakorlatijegy(85)
        self.assertGreaterEqual(teszt, "Jeles")

    def test_jo(self):
        teszt = gyakorlatijegy(84)
        self.assertGreaterEqual(teszt, "Jó")
    def test_jo_also(self):
        teszt = gyakorlatijegy(70)
        self.assertGreaterEqual(teszt, "Jó")

    def test_kozepes(self):
        teszt = gyakorlatijegy(69)
        self.assertGreaterEqual(teszt, "Közepes")
    def test_kozepes_also(self):
        teszt = gyakorlatijegy(55)
        self.assertGreaterEqual(teszt, "Közepes")

    def test_elegseges(self):
        teszt = gyakorlatijegy(54)
        self.assertGreaterEqual(teszt, "Elégséges")
    def test_esegseges_also(self):
        teszt = gyakorlatijegy(40)
        self.assertGreaterEqual(teszt, "Elégséges")

    def test_elegtelen(self):
        teszt = gyakorlatijegy(39)
        self.assertGreaterEqual(teszt, "Elégtelen")
    def test_elegtelen_also(self):
        teszt = gyakorlatijegy(0)
        self.assertGreaterEqual(teszt, "Elégtelen")

    def test_null_alatti(self):
        teszt = gyakorlatijegy(-2)
        self.assertEqual(teszt, "Érvénytelen érték")

unittest.main()

    
    

