import unittest

def armstrong_szam(szam: int) -> bool:
    szoveg = str(szam)
    hatvany = len(szoveg)
    osszeg = 0

    for karakter in szoveg:
        osszeg += int(karakter) ** hatvany

    return osszeg == szam



class TestArmstrongSzam(unittest.TestCase):

    def test_armstrong_szam(self):
        self.assertTrue(armstrong_szam(153))
        self.assertTrue(armstrong_szam(370))



unittest.main()