print("Működik a Git?")
print("Mindjárt kiderül!")

print("össezge_____________________")
szamok=[3,4,2,7,8,1,9,7,3,3,5,6,8,2,5,6,8,4,7,6,3,9,4,6,3,7,9,4,6,2,3,5,3]
osszeg=0
for x in szamok:
    osszeg=osszeg+x
    print(osszeg)
print(osszeg)
print("ven e 1 es_____________________")
vane =False
for x in szamok:
    if (x==1):
        vane=True
print(vane)
print("3 as db számai_____________________")
db=0
for x in  szamok:
    if (x==3):
        db=db+1;
print(db)
print("páros számok összege_____________________")
osszeg=0
for x in szamok:
    if x%2==0 :
        osszeg=osszeg+x
print(osszeg)
print("minimum kiválasztás tétele_____________________")
min=1000
for x in szamok:
    if x<min:
        min=x
print(min)
print("maximum_____________________")
max=-1000000
for x in szamok:
    if x>max:
        max=x
print(max)
print("új feladat__________________________________________________________________________\/")
numbers=[3,5,45,54,56,65,86,76,4,35,93]
valt=0
atlag=0
for x in numbers:
    valt=valt+x
    atlag=valt / 10
print(atlag)
print("_____________________")
min=1000
for x in numbers:
    if x<min:
        min=x
print(min)
print("_____________________")
max=-1000000
for x in szamok:
    if x>max:
        max=x
print(max)
print("_____________________")
paros=False
for x in numbers:
    if x%2==0 :
        paros=True
        print(paros)
print("_____________________")
otven=0
for x in numbers:
    if x>50 :
        otven=otven+x
print(otven)
print("_____________________")
k=False
for x in numbers:
    if x==9:
        k=True
        print(kilenc)
