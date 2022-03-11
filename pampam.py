from math import*
def aprLaukums(r):
    S=pi*r**2
    return S
# r1=int(input("Ievadiet riņķa laukumu \n"))
# rez1=aprLaukums(r1)
# r2=int(input("Ievadiet riņķa laukumu \n"))
# rez2=aprLaukums(r2)
# print("Laukumi ar pirmo r",rez1, "un ar otru", rez2) 

for r in range(1,10,2):
    rez=aprLaukums(r) 
    print("Laukums ar r", r, "m ir", rez, "kvm")