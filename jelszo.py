import unittest

def jelsz_erosseg(jelszo):
    erosseg = 1
    if len(jelszo) >= 5:
        erosseg += 1


    if len(jelszo) >= 8:
        erosseg += 2

    spec_karakter = ["_", "-", "."]

    for i in jelszo:
        if i in spec_karakter:
            erosseg += 2
        
    
    if "jelszo" in jelszo or "123" in jelszo:
        erosseg = 0
    
    if len(jelszo) == 0:
        erosseg = 0
    
    return erosseg

#jelszo = input("Input: ")

#print(jelsz_erosseg(jelszo))

class TesztJelszo(unittest.TestCase):
    def test_pelda(self):
        fgv = jelsz_erosseg("hazi_macska_4_life")
        self.assertEqual(fgv, 10)

unittest.main()