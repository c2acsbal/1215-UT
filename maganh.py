def maganhango_torl(szoveg):
    maganhanzok = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]

    modszoveg = ""
    for i in szoveg:
        if i not in maganhanzok:
            modszoveg += i
    
    return modszoveg

szoveg = input("Intput: ")

print(maganhango_torl(szoveg))
        