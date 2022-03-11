def noteiktinterval(d1,d2,sk):
    rezultats="Nepieder intervalam"
    if sk>=d1 and sk<=d2:
        rezultats="Skaitlis atrodas intervālā"
    return rezultats

d1=int(input("Ievadiet intervāla sākumu\n"))
d2=int(input("Ievadiet intervāla beigas\n"))
sk=int(input("Ievadiet skitli\n"))

rez=noteiktinterval(d1,d2,sk) 
print(rez)