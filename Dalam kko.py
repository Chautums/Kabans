
def dalAtl(a,b):
    if b==0: return "Ar 0 dalīt nevar"
    else: return a/b, a//b, a%b
x=int(input("Ievadi x \n")) 
y=int(input("Ievadi y \n"))
da= dalAtl(x,y)
print(da)  