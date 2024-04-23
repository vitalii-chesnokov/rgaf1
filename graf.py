from tkinter import *
from tkinter import simpledialog as sd
import  matplotlib.pyplot as plt
import numpy  #X vahemik X[min,max]
def Vaal():
    """Joonestatakse vaal paraabolite abil matplotlib mooduli kasutades
    """
    x1=numpy.arange(0,9,0.5)
    y1=(2/27)*x1**2-3
    x2=numpy.arange(-10,0,0.5)
    y2=0.04*x2**2-3
    x3=numpy.arange(-9,-4,0.5)
    y3=(2/4)*(x3+6)**2+1
    x4=numpy.arange(-3,9,0.5)
    y4=-(1/12)*(x4-3)**2+6
    x5=numpy.arange(5,8.3,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=numpy.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=numpy.arange(-13,-9,0.5)
    y7=-(0.75)*(x7+11)**2+6
    x8=numpy.arange(-15,-13,0.5)
    y8=-(0.5)*(x8+13)**2+3 
    x9=numpy.arange(-15,-10,0.5) #min,max, steep
    y9=[1]*len(x9)
    x10=numpy.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    #plt.plot(x1,y1,"r:*",x2,y2,"m-s")
    for i in range(1,11):
        plt.plot(eval(f"x{i}"), eval(f"y{i}"))
    plt.title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def Prillid():
    """
    """
    x1=numpy.arange(-9,-1,0.7)
    y1=-(1/16)*(x1+5)**2+2
    x2=numpy.arange(1,9,0.7)
    y2=-(1/16)*(x2-5)**2+2
    x3=numpy.arange(-9,-1,0.7)
    y3=(1/4)*(x3+5)**2-3
    x4=numpy.arange(1,9,0.7)
    y4=(1/4)*(x4-5)**2-3
    x5=numpy.arange(-9,-6,0.7)
    y5=-(x5+7)**2+5
    x6=numpy.arange(6,9,0.7)
    y6=-(x6-7)**2+5
    x7=numpy.arange(-1,1,0.7)
    y7=-(0.5*x7)**2+1.5
    plt.figure()
    for i in range(1,8):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"))
    plt.title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def Vihmavari():
    """
    """
    x1=numpy.arange(-12,12,0.7)
    y1=-(1/18)*x1**2+12
    x2=numpy.arange(-4,4,0.7)
    y2=-(1/8)*x2**2+6
    x3=numpy.arange(-12,-4,0.7)
    y3=-(1/8)*(x2+8)**2+6
    x4=numpy.arange(4,12,0.7)
    y4=-(1/8)*(x4-8)**2+6
    x5=numpy.arange(-4,-0.3,0.7)
    y5=2*(x5+3)**2-9
    x6=numpy.arange(-4,-0.2,0.7)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    for i in range(1,7):
        plt.plot(eval(f"x{i}"),eval(f"y{i}")) #plt.plot(eval(f"x{i}"), eval(f"y{i}"))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
def Liblikas():
    """
    """
    x1=numpy.arange(-9,-1,0.7)
    y1=-(1/8)*(x1+9)**2+8
    x2=numpy.arange(1,9,0.7)
    y2=-(1/8)*(x2-9)**2+8
    x3=numpy.arange(-9,-8,0.7)
    y3=7*(x3+8)**2+1
    x4=numpy.arange(8,9,0.7)
    y4=7*(x4-8)**2+1
    x5=numpy.arange(-8,-1,0.7)
    y5=(1/49)*(x5+1)**2
    x6=numpy.arange(1,8,0.7)
    y6=(1/49)*(x6-1)**2
    x7=numpy.arange(-8,-1,0.7)
    y7=-(4/49)*(x7+1)**2
    x8=numpy.arange(1,8,0.7)
    y8=-(4/49)*(x8-1)**2
    x9=numpy.arange(-8,-2,0.7)
    y9=(1/3)*(x9+5)**2-7
    x10=numpy.arange(-2,8,0.7)
    y10=(1/3)*(x10-5)**2-7
    x11=numpy.arange(-2,-1,0.7)
    y11=-2*(x11+1)**2-2
    x12=numpy.arange(1,2,0.7)
    y12=-2*(x12-1)**2-2
    x13=numpy.arange(-1,1,0.7)
    y13=-4*(x13)**2+2
    x14=numpy.arange(-1,1,0.7)
    y14=4*(x14)**2-6
    x15=numpy.arange(-2,0,0.7)
    y15=-1.5*(x15)+2
    x16=numpy.arange(0,2,0.7)
    y16=1.5*(x16)+2
    plt.figure()
    for i in range(1,17):
        plt.plot(eval(f"x{i}"),eval(f"y{i}")) #plt.plot(eval(f"x{i}"), eval(f"y{i}"))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
def Kilpkonn():
    x1=numpy.arange(-7, 7, 0.5)
    y1=(-3/49) * x1**2 + 8
    x2=numpy.arange(-7, 7, 0.5)
    y2=(4/49) * x2**2 + 1
    x3=numpy.arange(-6.8, -2,0.5)
    y3=-0.75 * (x3 + 4)**2 + 11
    x4=numpy.arange(2, 6.8,0.5)
    y4=-0.75 * (x4 - 4)**2 + 11
    x5=numpy.arange(-5.8,-2.8,0.5)
    y5=-(x5 + 4)**2 + 9
    x6=numpy.arange(2.8,5.8,0.5)
    y6=-(x6 - 4)**2 + 9
    x7=numpy.arange(-4, 4, 0.5)
    y7=(4/9) * x7**2 - 5
    x8=numpy.arange(-5.2,5.2,0.5)
    y8=(4/9) * x8**2 - 9
    x9=numpy.arange(-7, -2.8,0.5)
    y9=(-1/16) * (x9 + 3)**2 - 6
    x10=numpy.arange(2.8, 7, 0.5)
    y10=(-1/16) * (x10 - 3)**2 - 6
    x11=numpy.arange(-7, 0, 0.5)
    y11=(1/9) * (x11 + 4)**2 - 11
    x12=numpy.arange(0, 7, 0.5)
    y12=(1/9) * (x12 - 4)**2 - 11
    x13=numpy.arange(-7,-4.5, 0.5)
    y13=-(x13 + 5)**2
    x14=numpy.arange(4.5, 7, 0.5)
    y14=-(x14 - 5)**2
    x15=numpy.arange(-3, 3, 0.5)
    y15=(2/9) * x15**2 + 2
    plt.figure()
    plt.plot(x1,y1,"m-*",x2,y2,"m-*",x3,y3,"m-*",x4,y4,"m-*",x5,y5,"m-*",x6,y6,"m-*",x7,y7,"m-*",x8,y8,"m-*",x9,y9,"m-*",x10,y10, "m-*",x11,y11,"m-*",x12,y12,"m-*",x13,y13,"m-*",x14,y14,"m-*",x15,y15,"m-*")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
#def valik(event):
#    eval(f"{loetelu.get(loetelu.curselection())}()")

    
#aken=Tk()
#aken.geometry("400x500")
#aken.title("Akna pealkiri")
#aken.configure(bg="#13e0eb")
#l=["Vaal","Vihmavari","Liblikas","Prillid","Kilpkonn"]
#loetelu=Listbox(aken,font="Arial 30",fg="green",bg="gold",selectborderwidth=3,selectbackground="lightblue")
#for i in range(len(l)):
#    loetelu.insert(i,l[i])

#loetelu.grid()
#loetelu.bind("<Double-1>",valik)

#aken.mainloop()


aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#DCDCDC")
aken.iconbitmap("icon.ico") 
raam=Frame(aken)
vl=Button(raam,
            text="Vaal",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Vaal)
pr=Button(raam,
          text="Prillid",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Prillid)
vh=Button(raam,
            text="Vihmavari",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Vihmavari)
lb=Button(raam,
            text="Liblikas",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Liblikas)
kl=Button(raam,
            text="Kilpkonn",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Kilpkonn)
raam.pack()
vl.grid(row=0, column=0)
pr.grid(row=1,column=0)
vh.grid(row=2, column=0)
lb.grid(row=3,column=0)
kl.grid(row=4,column=0)
aken.mainloop()