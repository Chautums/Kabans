def summa(a,b):
    return ((a*b)+(a/b))
a=int(input("Ievadi 1. skaitli\n")) 
b=int(input("Ievadi 2. skaitli\n"))
y=(summa(a,b)+6*summa(a,b)-summa(a,b)**2)/summa(a,b)
print(y)