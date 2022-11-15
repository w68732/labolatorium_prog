import random
n = int(input("wprowadz liczbe"))
zestaw_1=[]
while n>0:
    zestaw_1.append(random.randrange(0, 11))
    n-=1
    print(zestaw_1)
zestaw_2=[]
m = int(input("wprowadz liczbe"))
for i in range(m):
    zestaw_2.append(random.randrange(5, 16))
    print(zestaw_2)
t = int(input("jaka liczba"))
if t in zestaw_1:
    print("liczba z zestawu1")
elif t in zestaw_2:
    print("liczba z zestawu2")
else:
    print("w zestawach nie ma takiej liczby")
