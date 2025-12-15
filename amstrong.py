bekertHossz = input("Kérek egy számot: ")
bekert = int(bekertHossz)
ossz = 0

for i in range(len(bekertHossz)):
    ossz += int(bekertHossz[i]) ** len(bekertHossz)

if ossz == bekert:
    print("Ez egy Armstrong szám!")
else:
    print("Ez NEM egy Armstrong szám!")