from tkinter import *
# from tkinter import _ButtonCommand
mansLogs=Tk()
mansLogs.title("Mans kalkulators")   #Loga virsraksts
mansLogs.iconbitmap("ginger.ico")   #ikoniņa logam
mansLogs.geometry("450x300")   #loga izmēri

cheks=Tk()
cheks.title("Čeks")
cheks.geometry("250x400")



def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0


def btnCommand(command):
    global num1  #mainīgais tiek izmantots visai programmai 
    global mathOp
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Equals(): 
    num2=int(e.get())
    result=0
    # if mathOp=="+":    #ja lietotājs nospiež +, tad kalkulators saskaita skaitļus
    #     result=num1 + num2
    # elif mathOp=="-":
    #     result=num1-num2
    # elif mathOp=="*":
    #     result=num1*num2
    # elif mathOp=="/":
    #     result=num1/num2
    if mathOp=="+":
        result=num2
        el.insert(0, " Pārtika")
    elif mathOp=="-":
        result=num1+num2
        el.insert(0, " Sadzīves preces")
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    el.insert(0,str(result))
    return 0

def clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0
e=Entry(mansLogs, width=10, font=("Arial Black", 24))  #lodziņš kurā rādās cipari kurus uzraksta
el=Entry(cheks,width=10, font=("Arial Black", 16)) 

btn0=Button(mansLogs, text="0",padx="40", pady="20",command=lambda:btnClick(0))   #izveidojam pogu
btn1=Button(mansLogs, text="1",padx="40", pady="20",command=lambda:btnClick(1))
btn2=Button(mansLogs, text="2",padx="40", pady="20",command=lambda:btnClick(2))
btn3=Button(mansLogs, text="3",padx="40", pady="20",command=lambda:btnClick(3))
btn4=Button(mansLogs, text="4",padx="40", pady="20",command=lambda:btnClick(4))
btn5=Button(mansLogs, text="5",padx="40", pady="20",command=lambda:btnClick(5))
btn6=Button(mansLogs, text="6",padx="40", pady="20",command=lambda:btnClick(6))
btn7=Button(mansLogs, text="7",padx="40", pady="20",command=lambda:btnClick(7))
btn8=Button(mansLogs, text="8",padx="40", pady="20",command=lambda:btnClick(8))
btn9=Button(mansLogs, text="9",padx="40", pady="20",command=lambda:btnClick(9))  # ,command=lambda:btnClick(0) izdara tā, lai poga strādātu
# btnAdd=Button(mansLogs, text="+",padx="40", pady="20",command=lambda:btnCommand("+"))
# btnSub=Button(mansLogs, text="-",padx="40", pady="20",command=lambda:btnCommand("-"))
# btnRez=Button(mansLogs, text="*",padx="40", pady="20",command=lambda:btnCommand("*"))
# btnDal=Button(mansLogs, text="/",padx="40", pady="20",command=lambda:btnCommand("/"))
btnEqual=Button(mansLogs, text="=",padx="40", pady="20", bg="#44D807", command=Equals)
btnClear=Button(mansLogs, text="C",padx="40", pady="20", bg="#FF1C26", command=clear)

btnPartika=Button(mansLogs, text="Pārtika",padx="60", pady="20",command=lambda:btnCommand("+"))
btnSapr=Button(mansLogs, text="Sadz. Preces",padx="40", pady="20",command=lambda:btnCommand("-"))
btnKim=Button(mansLogs, text="Ķīmija",padx="60", pady="20",command=lambda:btnClick())
btnZales=Button(mansLogs, text="Zāles",padx="60", pady="20",command=lambda:btnClick())





e.grid(row=0,column=0, columnspan=4)  #kalkulatora "ekrāniņš"
el.grid(row=0, column=0,columnspan=4)

btn7.grid(row=3, column=0)  #pogu atrašanās vieta 
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

btn0.grid(row=4, column=1)

# btnAdd.grid(row=4, column=1)
# btnSub.grid(row=4, column=2)
# btnRez.grid(row=3, column=3)
# btnDal.grid(row=2, column=3)

btnClear.grid(row=4, column=0)
btnEqual.grid(row=4, column=2)  #rowspan un columnspan apvieno rindas un kolonnas
 
btnPartika.grid(row=4, column=4)
btnSapr.grid(row=3, column=4)
btnKim.grid(row=2, column=4)
btnZales.grid(row=1, column=4)

mansLogs.mainloop()  #izdara tā, lai logs neaizveras pats par sevi 
