def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True
    else:
        return False

db = 0
osszeg = 0
for i in range(100, 1000):
    if oszthato(i):
        db += 1
        osszeg += i
atlag = osszeg / db
print(f"A 7-el osztható és 3-al nem osztható számok átlaga: {atlag}")