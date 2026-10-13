import unittest
def parosszamokosszeg(szam1: int, szam2: int):
    szamlalo = 0
    for i in range(szam1-1, szam2+1):
        if i % 2 == 0:
            szamlalo += i
    return f"A(z) [{szam1}; {szam2}] intervallumban eső páros számok összege: {szamlalo}"

class evennumberstestFunction(unittest.TestCase):
    def test_two_even(self):
        teszt = 2, 4
        self.assertEqual(teszt, 6)

    def test_two_odd(self):
        teszt = 3, 5
        self.assertEqual(teszt, 4)

    def test_two_diff(self):
        teszt = 2, 3
        self.assertEqual(teszt, 2)
unittest.main()