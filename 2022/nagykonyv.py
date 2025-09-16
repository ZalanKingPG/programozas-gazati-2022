f = open("konyvek", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class konyv:
    def __init__(self, nev, szulEv, halEv, nemzetiseg, cim, helyezes):
        self.nev = nev
        self.szulEv = int(szulEv)
        self.halEv = int(halEv)
        self.nemzetiseg = nemzetiseg
        self.cim = cim
        self.helyezes = int(helyezes)

#1. feladat
adatok = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    if darabok[2] == "":
        darabok[2] = 2005
    a = konyv(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    adatok.append(a)
#2. feladat
print(f"3.2 feladat: Az állományban {len(adatok)} könyv adatai szerepelnek.")
#3. feladat
elso = 1000
maxi = 0
for i in range(len(adatok)):
    if adatok[i].helyezes < elso:
        elso = adatok[i].helyezes
        maxi = i
print(f"3.3 feladat: A legjobb helyezest elert {adatok[maxi].nemzetiseg} könyv: {adatok[maxi].nev}: {adatok[maxi].cim}")
#4. feladat
volt = False
for i in range(len(adatok)):
    if adatok[i].nemzetiseg == "német":
        volt = True
        break
if volt:
    print("3.4 feladat: A listában szerpel német író könyve.")
else:
    print("3.4 feladat: A listában nem szerpel német író könyve.")
#5. feladat
print(f"3.5 feladat: 90 évesnél idősebb írók:")
koltok = set()
for i in range(len(adatok)):
    if adatok[i].halEv - adatok[i].szulEv > 90:
        koltok.add(adatok[i].nev)
for i in koltok:
    print(f"\t{i}")