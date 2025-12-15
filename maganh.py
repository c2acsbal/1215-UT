import unittest

def maganhango_torl(szoveg):
    maganhanzok = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]

    modszoveg = ""
    for i in szoveg:
        if i not in maganhanzok:
            modszoveg += i
    
    return modszoveg

szoveg = input("Intput: ")

print(maganhango_torl(szoveg))

class Tesztmaganh(unittest.TestCase):
    def test_pelda(self):
        fgv = maganhango_torl("Iden Java szigeten voltunk nyaralni.")
        self.assertEqual(fgv, "dn Jv szgtn vltnk nyrln.")

unittest.main()
        