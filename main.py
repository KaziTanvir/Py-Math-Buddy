from tkinter import*
import math

var = Tk()
var.title("Math Buddy")
var.configure(bg="#ffa56e")
e = Entry(var, width=60,  borderwidth=20)
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

# Backend
# creating buttom functions
def thebutton(numone):
    thecurrent = e.get()
    e.delete(0, END)
    e.insert(0,str(thecurrent)+str(numone))
def thebuttonclear():
    e.delete(0,END)
def thebuttonadd():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "addition"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonequal():
    num2 = e.get()
    e.delete(0,END)
    if mathematics == "addition":
        e.insert(0, functionnum + int(num2))
    if mathematics == "substraction":
        e.insert(0, functionnum - int(num2))
    if mathematics == "multiplication":
        e.insert(0, functionnum * int(num2))
    if mathematics == "division":
        e.insert(0, functionnum / int(num2))
    if mathematics == "raisedto":
        e.insert(0, functionnum ** int(num2))
    if mathematics == "squareroot":
        e.insert(0, math.sqrt(functionnum))
    if mathematics == "percentage":
        e.insert(0, functionnum/100)
    if mathematics == "sin":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.sin(rad))
    if mathematics == "cos":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.cos(rad))
    if mathematics == "tan":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.tan(rad))
    if mathematics == "csc":
        rad = functionnum * (math.pi/180)
        e.insert(0, 1/math.sin((rad)))
    if mathematics == "sec":
        rad = functionnum * (math.pi/180)
        e.insert(0, 1/math.cos((rad)))
    if mathematics == "cot":
        rad = functionnum * (math.pi/180)
        e.insert(0, 1/math.tan((rad)))
    if mathematics == "ave":
        e.insert((functionnum +int(num2))/2)
    if mathematics == "square":
        e.insert(0, functionnum**2)
    if mathematics == "cube":
        e.insert(0, functionnum**3)
    if mathematics == "naturallog":
        e.insert(0, math.log(functionnum))
    if mathematics == "e":
        e.insert(0, math.exp(functionnum))
    if mathematics == "log":
        e.insert(0, math.log10(functionnum))
    if mathematics == "negative":
        e.insert(0, functionnum * -1)
    if mathematics == "absolutevalue":
        e.insert(0, abs(functionnum))
    if mathematics == "factorial":
        e.insert(0, math.factorial(functionnum))
    if mathematics == "2raisedto":
        e.insert(0, 2 **functionnum)
    if mathematics == "inverse":
        e.insert(0, functionnum**(-1))
    if mathematics == "sininverse":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.asin(rad))
    if mathematics == "cosinverse":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.acos(rad))
    if mathematics == "taninverse":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.atan(rad))
def thebuttonsubstract():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "substraction"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonmultiplication():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "multiplication"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttondivision():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "division"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonraisedtopowerof():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "raisedto"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonsquareroot():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "squareroot"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonpercent():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "percentage"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonsin():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sin"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttoncos():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cos"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttontan():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "tan"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttoncsc():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "csc"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonsec():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sec"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttoncot():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cot"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonaverage():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "ave"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonsquare():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "square"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttoncube():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cube"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonln():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "naturallog"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonetothex():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "e"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonlog():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "log"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonnegative():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "negative"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonabsoulutevalue():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "absolutevalue"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonfactorial():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "factorial"
    functionnum = int(num1)
    e.delete(0,END)
def thebutton2raisedto():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "2raisedto"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttoninverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "inverse"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttonsininverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sininverse"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttoncosinverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cosinverse"
    functionnum = int(num1)
    e.delete(0,END)
def thebuttontaninverse():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "taninverse"
    functionnum = int(num1)
    e.delete(0,END)

# Frontend
# Button Creation

button1 = Button(var, text="1", padx = 20, pady = 10, command = lambda: thebutton(1))
button2 = Button(var, text="2", padx = 20, pady = 10, command = lambda: thebutton(2))
button3 = Button(var, text="3", padx = 20, pady = 10, command = lambda: thebutton(3))
button4 = Button(var, text="4", padx = 20, pady = 10, command = lambda: thebutton(4))
button5 = Button(var, text="5", padx = 20, pady = 10, command = lambda: thebutton(5))
button6 = Button(var, text="6", padx = 20, pady = 10, command = lambda: thebutton(6))
button7 = Button(var, text="7", padx = 20, pady = 10, command = lambda: thebutton(7))
button8 = Button(var, text="8", padx = 20, pady = 10, command = lambda: thebutton(8))
button9 = Button(var, text="9", padx = 20, pady = 10, command = lambda: thebutton(9))
button0 = Button(var, text="0", padx = 20, pady = 10, command = lambda: thebutton(0))

buttonpi = Button(var, text="π", padx = 20, pady = 10, command = lambda: thebutton(math.pi))
thebuttonadd = Button(var, text="+", padx = 20, pady = 10, command = thebuttonadd)
thebuttonequal = Button(var, text="=", padx = 20, pady = 10, command = thebuttonequal)
thebuttonclear = Button(var, text="clear", padx = 20, pady = 10, command = thebuttonclear)
thebuttonsubstract = Button(var, text="-", padx = 20, pady = 10, command = thebuttonsubstract)
thebuttonmultiplication = Button(var, text="x", padx = 20, pady = 10, command = thebuttonmultiplication)
thebuttondivision = Button(var, text="/", padx = 20, pady = 10, command = thebuttondivision)
thebuttonraisedtopowerof = Button(var, text="x^y", padx = 20, pady = 10, command = thebuttonraisedtopowerof)
thebuttonsquareroot = Button(var, text="√", padx = 20, pady = 10, command = thebuttonsquareroot)
thebuttonpercent = Button(var, text="%", padx = 20, pady = 10, command = thebuttonpercent)

thebuttonsin = Button(var, text="sin", padx = 20, pady = 10, command = thebuttonsin)
thebuttoncos = Button(var, text="cos", padx = 20, pady = 10, command = thebuttoncos)
thebuttontan = Button(var, text="tan", padx = 20, pady = 10, command = thebuttontan)
thebuttoncsc = Button(var, text="csc", padx = 20, pady = 10, command = thebuttoncsc)
thebuttonsec = Button(var, text="sec", padx = 20, pady = 10, command = thebuttonsec)
thebuttoncot = Button(var, text="cot", padx = 20, pady = 10, command = thebuttoncot)
thebuttonaverage = Button(var, text="ave", padx = 20, pady = 10, command = thebuttonaverage)
thebuttonsquare = Button(var, text="x^2", padx = 20, pady = 10, command = thebuttonsquare)
thebuttoncube = Button(var, text="x^3", padx = 20, pady = 10, command = thebuttoncube)

thebuttonln = Button(var, text="ln", padx = 20, pady = 10, command = thebuttonln)
thebuttonetothex = Button(var, text="e^x", padx = 20, pady = 10, command = thebuttonetothex)
thebuttonlog = Button(var, text="log", padx = 20, pady = 10, command = thebuttonlog)
thebuttonnegative = Button(var, text="(-)", padx = 20, pady = 10, command = thebuttonnegative)
thebuttonabsoulutevalue = Button(var, text="|x|", padx = 20, pady = 10, command = thebuttonabsoulutevalue)
thebuttonfactorial = Button(var, text="!", padx = 20, pady = 10, command = thebuttonfactorial)
thebutton2raisedto = Button(var, text="2^x", padx = 20, pady = 10, command = thebutton2raisedto)
thebuttoninverse = Button(var, text="x^-1", padx = 20, pady = 10, command = thebuttoninverse)
thebuttonsininverse = Button(var, text="sin(x)^-1", padx = 20, pady = 10, command = thebuttonsininverse)
thebuttoncosinverse = Button(var, text="cos(x)^-1", padx = 20, pady = 10, command = thebuttoncosinverse)
thebuttontaninverse = Button(var, text="tan(x)^-1", padx = 20, pady = 10, command = thebuttontaninverse)

# Button Location
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
thebuttonabsoulutevalue.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
thebuttonnegative.grid(row=2,column=3)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonpi.grid(row=3,column=3)
button0.grid(row=4,column=0)

thebuttonclear.grid(row=4,column=1)
thebuttonfactorial.grid(row=4,column=2)
thebuttonlog.grid(row=4,column=3)
thebuttonadd.grid(row=5,column=0)
thebuttonequal.grid(row=5,column=1)
thebutton2raisedto.grid(row=5,column=2)
thebuttonetothex.grid(row=5,column=3)
thebuttonsubstract.grid(row=6,column=0)
thebuttonmultiplication.grid(row=6,column=1)
thebuttondivision.grid(row=6,column=2)

thebuttonln.grid(row=6,column=3)
thebuttoninverse.grid(row=10,column=0)
thebuttonraisedtopowerof.grid(row=7,column=0)
thebuttonsquareroot.grid(row=7,column=1)
thebuttonpercent.grid(row=7,column=2)
thebuttonsquare.grid(row=7,column=3)
thebuttoncosinverse.grid(row=10,column=1)
thebuttonsin.grid(row=8,column=0)
thebuttoncos.grid(row=8,column=1)
thebuttontan.grid(row=8,column=2)
thebuttoncube.grid(row=8,column=3)
thebuttontaninverse.grid(row=10,column=2)
thebuttoncsc.grid(row=9,column=0)
thebuttonsec.grid(row=9,column=1)
thebuttoncot.grid(row=9,column=2)
thebuttonsin.grid(row=8,column=0)
thebuttonaverage.grid(row=9,column=3)
thebuttonsininverse.grid(row=10,column=3)

var.mainloop()










    
   
    
    
    
    
    



