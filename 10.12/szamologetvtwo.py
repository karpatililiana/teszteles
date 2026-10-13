import unittest
def szamologepvtwo(elso: float, masodik: float, muvelet):
    if muvelet != "*" or muvelet != "+" or muvelet != "-" or muvelet != "/":
        if muvelet == "*":
            print(round(elso * masodik, 2))
        elif muvelet == "-":
            print(round(elso - masodik, 2))
        elif muvelet == "+": 
            print(round(elso + masodik, 2))
        elif muvelet == "/":
            if masodik == 0:
                return "Ejnye, nullával nem osztunk"
            else:
                return round(elso / masodik, 2)
    else:
        return "Hibás műveleti jel!"

class CalculatorvtwoFunction(unittest.TestCase):
    def test_rossz_jel(self):
        teszt = szamologepvtwo(5.00, 3.00, ":")
        self.assertEqual(teszt, "Hibás műveleti jel!")

    def test_null_osztas(self):
        teszt = szamologepvtwo(3.00, 0.00, "/")
        self.assertEqual(teszt, "Ejnye, nullával nem osztunk")

    def test_normal_osztas(self):
        teszt = szamologepvtwo(6.00, 2.00, "/") 
        self.assertEqual(teszt, 3)

    def test_normal_szorzas(self):
        teszt = szamologepvtwo(2.00, 3.00, "*")
        self.assertEqual(teszt, 6.00)

    def test_normal_osszeadas(self):
        teszt = szamologepvtwo(1.00, 2.00, "+")
        self.assertEqual(teszt, 3.00)

    def test_noraml_kivonas(self):
        teszt = szamologepvtwo(5.00, 3.00, "-")
        self.assertEqual(teszt, 2.00) 

unittest.main()

