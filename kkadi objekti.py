# class person:
#     def set (self, name, age): # metodes definēšana
#         self.name=name # tiek izveidots lauks name
#         self.age=age # izveidots lauks age
#     def output(self): # metodes definēšana
#         print(self.name, self.age)
# p=person() # objektu izveidošana
# person.set(p,"Peter",20)
# person.output(p)


# class person:
#     def set(self, name, age): 
#         self.__name=name #šeit tiek izveidots slēptais lauks name
#         self.__age=age #seit tiek izveidots slēptais lauks age
#     def output (self) :
#         print(self.__name, self.__age)
# p=person()
# p.set("Peter", 20)
# print(p.__name) #nevar piekļūt slēptajam laukam, izmet kļūdu
# p.output()


# class person:
#     def set(self, name, age): 
#         self.__name=name #šeit tiek izveidots slēptais lauks name
#         self.__age=age #seit tiek izveidots slēptais lauks age
#     def output (self) :
#         print(self.__name, self.__age)
# p=person()
# p.set("Peter", 20)
# print(p._person__name) #var piekļūt slēptajam laukam
# p.output()



# class person:
#     def __init__(self,name,age): #konstruktora definēšana
#         self.name=name #izveido lauku name
#         self.age=age #izveido lauku age
#     def output(self): #metodes definēšana
#         print(self.name,self.age)
#     def __del__(self):  #destruktora definēšana 
#         print("Deleted:", self.name, self.age)
# p=person("Peter",20) #objekta izveidošana un konstruktora izsaukšana
# p.output()
# del p #objekta likvidēšana un destruktora izsaukšana


class person:
    counter=0 #klases līmeņa lauks
    def __init__(self,name,age):
        