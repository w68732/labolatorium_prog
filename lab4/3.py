zwierzęta = []
y = 0
while y < 4:
    a = input("Podaj nazwy zwierząt: ")
    zwierzęta.append(a)
    y += 1
print(zwierzęta)
zwierzęta.sort()
print(zwierzęta)
print(zwierzęta[0], zwierzęta[-3:])
a = sorted(zwierzęta)
print(a)
print(len(zwierzęta))