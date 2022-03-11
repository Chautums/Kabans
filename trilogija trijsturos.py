def lenkuParbaude(len1,len2,len3):
    rezultats=False
    if len1+len2+len3==180:
        rezultats=True
    return rezultats

len1=int(input("Ievadi 1. leņķi\n")) 
len2=int(input("Ievadi 2. leņķi\n")) 
len3=int(input("Ievadi 3. leņķi\n")) 
rez=lenkuParbaude(len1, len2, len3)
if rez:
    print("Trijstūris eksistē")
else: 
    print("Trijstūris neeksistē")