import random
# punkty = []
# for b in range(15):
#     a = random.uniform(0, 50)
#     c = round(a, 2)
#     punkty.append(c)
punkty = [round(random.uniform(0, 50), 2) for b in range(15)]
print(punkty)
print("maksymalna liczba punktów: ", max(punkty))
print("minimalna liczba punktów: ", min(punkty))
d = float(input("Podaj liczbe: "))
if d in punkty:
    print("wartość w indeksie: ", punkty.index(d))
else:
    print("brak wartości w liscie")

e = sum(punkty) / len(punkty)
print("średnia liczb: ", e)
round(e, 2)

lista1 = []
for i in punkty:
    if i < e:
        lista1.append(i)
print(len(lista1))
print(lista1)

lista2 = [i for i in punkty if i > e]
print(len(lista2))
print(lista2)

