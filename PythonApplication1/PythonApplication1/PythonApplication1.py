print("Működik a Git?")
print("Mindjárt kiderül!")

print("_____________________")
szamok=[3,4,2,7,8,1,9,7,3]
osszeg=0
for x in szamok:
    osszeg=osszeg+x
    print(osszeg)
print(osszeg)
print("_____________________")
vane =False
for x in szamok:
    if (x==1):
        vane=True
print(vane)
print("_____________________")
db=0
for x in  szamok:
    if (x==3):
        db=db+1;
print(db)