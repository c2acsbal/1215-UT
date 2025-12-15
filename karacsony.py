print("kérek egy karifa szintezést: ", end="")
faszint = int(input())
space = 0
counter = 0
counter2 = 0
i = 0
a = 0
g = 0

while faszint+1 != counter2:
    print(" ",end="")
    counter2 = counter2 + 1

print("*",end="")
print("*")

counter2 = 0
jelenSzint = faszint
while faszint != counter:
    while jelenSzint != counter2:
        print(" ",end="")
        counter2 = counter2 + 1
    space = space + 1
    print("*", end="")
    while i != space*2:
        print("*", end="")
        i = i+1
    print("*")
    counter = counter + 1
    counter2 = 0
    jelenSzint = jelenSzint-1
    i = 0

a = 0
counter = 0
print("*", end="")
while a != space:
    print("*", end="")
    counter = counter + 1
    a = a + 1

print("||", end="")
a = 0
while a != space:
    print("*", end="")
    counter = counter + 1
    a = a + 1
print("*")

f = 0
while faszint+1 != f:
    while faszint+1 != g:
        print(" ", end="")
        g = g+1
    print("||")
    f = f+1
    g = 0