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