#4. uzdevums

lst=[]
n=int(input("Cik skaitļu būs sarakstā?\n"))
for i in range(0, n):
    print("Ievadi skaitli")
    ele = int(input())
    lst.append(ele)
print("Skaitļu summa ir", sum(lst)) 
a=sum(lst)/n
print("Vidējais aritmētiskais ir ",a)