def izdruka(daudzums, sar1):
    for element1 in range(0, daudzums):
        print(sar1[element1])
    # return 0
sar1=[1,2,3,4,5,6,7,8,9]
daudzums=int(input("Norādiet daudzumu"))
rez=izdruka(daudzums,sar1)
print(rez)

