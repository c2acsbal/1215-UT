mozgas = input("Kérek egy mozdulatsorozatot! ")
x = 0
y = 0

for i in range(len(mozgas)):
    if mozgas[i].upper() == "B":
        x -= 1
    elif mozgas[i].upper() == "J":
        x += 1
    elif mozgas[i].upper() == "F":
        y -= 1
    elif mozgas[i].upper() == "L":
        y += 1

if x > 0:
    print(f"Jobbra: {x}")
elif x < 0:
    print(f"Balra: {-x}")
else:
    print(f"Nem mozdult x irányba")

if y > 0:
    print(f"Fel: {y}")
elif y < 0:
    print(f"Le: {-y}")
else:
    print(f"Nem mozdult y irányba: {y}")