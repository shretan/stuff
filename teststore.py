from tkinter import *
import random
root=Tk()
root.geometry("700x700")
def store():
        x=random.randint(0,2000)
        randref=str(x)
        rand.set(randref)
    
        fries_code=50
        paneer_code=49
        pav_code=48
        burger_code=47
        chapati_code=46
        taco_code=45

        friescost=50
        paneercost=150
        pavcost=70
        burgercost = 59
        chapaticost=20
        tacocost=200
    
        if(fries.get==""):
            qfries=0
        else:
            qfries=float(fries.get())
        
        if(paneer.get==""):
            qpaneer=0
        else:
            qpaneer=float(paneer.get())
        
        if(chapati.get==""):
            qchapati=0
        else:
            qchapati=float(chapati.get())
        
        if(pav.get==""):
            qpav=0
        else:
            qpav=float(pav.get())
        
        if(taco.get==""):
            qtaco=0
        else:
            qtaco=float(taco.get())
        
        if(burger.get==""):
            qburger=0
        else:
            qburger=float(burger.get())
        
        chato=qchapati*chapaticost
        frato=qfries*friescost
        brato=qburger*burgercost
        tato=qtaco*tacocost
        pato=qpav*pavcost
        panto=qpaneer*paneercost
    
        f1=Tk()
        f1.geometry("700x700")
        tot=chato+frato+brato+tato+pato+panto
        totp=Label(f1,font=('arial', 16, 'bold'),text=tot).grid(row=8,column=4)
        totp=Label(f1,font=('arial', 16, 'bold'),text="come and eat again fat shit").grid(row=9,column=2)
    
        c=Label(f1,font=('arial', 16, 'bold'),text="code").grid(row=1,column=0)
        p=Label(f1,font=('arial', 16, 'bold'),text="product").grid(row=1,column=1)
        q=Label(f1,font=('arial', 16, 'bold'),text="quantity").grid(row=1,column=2)
        co=Label(f1,font=('arial', 16, 'bold'),text="cost/quantity").grid(row=1,column=3)
        to=Label(f1,font=('arial', 16, 'bold'),text="total").grid(row=1,column=4)
     
        c1=Label(f1,font=('arial', 16, 'bold'),text=fries_code).grid(row=2,column=0)
        p1=Label(f1,font=('arial', 16, 'bold'),text="fries").grid(row=2,column=1)
        q1=Label(f1,font=('arial', 16, 'bold'),text=qfries).grid(row=2,column=2)
        co1=Label(f1,font=('arial', 16, 'bold'),text=friescost).grid(row=2,column=3)
        to1=Label(f1,font=('arial', 16, 'bold'),text=frato).grid(row=2,column=4)
     
        c2=Label(f1,font=('arial', 16, 'bold'),text=paneer_code).grid(row=3,column=0)
        p2=Label(f1,font=('arial', 16, 'bold'),text="paneer").grid(row=3,column=1)
        q2=Label(f1,font=('arial', 16, 'bold'),text=qpaneer).grid(row=3,column=2)
        co2=Label(f1,font=('arial', 16, 'bold'),text=paneercost).grid(row=3,column=3)
        to2=Label(f1,font=('arial', 16, 'bold'),text=panto).grid(row=3,column=4)
     
        c3=Label(f1,font=('arial', 16, 'bold'),text=chapati_code).grid(row=4,column=0)
        p3=Label(f1,font=('arial', 16, 'bold'),text="chapati").grid(row=4,column=1)
        q3=Label(f1,font=('arial', 16, 'bold'),text=qchapati).grid(row=4,column=2)
        co3=Label(f1,font=('arial', 16, 'bold'),text=chapaticost).grid(row=4,column=3)
        to3=Label(f1,font=('arial', 16, 'bold'),text=chato).grid(row=4,column=4)
     
        c4=Label(f1,font=('arial', 16, 'bold'),text=burger_code).grid(row=5,column=0)
        p4=Label(f1,font=('arial', 16, 'bold'),text="burger").grid(row=5,column=1)
        q4=Label(f1,font=('arial', 16, 'bold'),text=qburger).grid(row=5,column=2)
        co4=Label(f1,font=('arial', 16, 'bold'),text=burgercost).grid(row=5,column=3)
        to4=Label(f1,font=('arial', 16, 'bold'),text=brato).grid(row=5,column=4)
     
        c5=Label(f1,font=('arial', 16, 'bold'),text=taco_code).grid(row=6,column=0)
        p5=Label(f1,font=('arial', 16, 'bold'),text="taco").grid(row=6,column=1)
        q5=Label(f1,font=('arial', 16, 'bold'),text=qtaco).grid(row=6,column=2)
        co5=Label(f1,font=('arial', 16, 'bold'),text=tacocost).grid(row=6,column=3)
        to5=Label(f1,font=('arial', 16, 'bold'),text=tato).grid(row=6,column=4)
     
        c6=Label(f1,font=('arial', 16, 'bold'),text=pav_code).grid(row=7,column=0)
        p6=Label(f1,font=('arial', 16, 'bold'),text="pav").grid(row=7,column=1)
        q6=Label(f1,font=('arial', 16, 'bold'),text=qpav).grid(row=7,column=2)
        co6=Label(f1,font=('arial', 16, 'bold'),text=pavcost).grid(row=7,column=3)
        to6=Label(f1,font=('arial', 16, 'bold'),text=pato).grid(row=7,column=4)
    
     
def rexit():
    root.destroy()
    
rand=StringVar()
fries=StringVar()
paneer=StringVar()
pav=StringVar()
burger=StringVar()
chapati=StringVar()
taco=StringVar()
rexit=StringVar()
storeid=Label(font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w").grid(row=0,column=0)
storeReference=Entry(font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,justify='right').grid(row=0,column=1)

lfries= Label(font=('arial', 16, 'bold'),text="fries",bd=16,anchor="w").grid(row=1, column=0)
efries=Entry(font=('arial',16,'bold'),textvariable=fries,bd=10,insertwidth=4,justify='right').grid(row=1,column=1)

lpaneer= Label(font=('arial', 16, 'bold'),text="paneerroll",bd=16,anchor="w").grid(row=2, column=0)
epanner=Entry(font=('arial',16,'bold'),textvariable=paneer,bd=10,insertwidth=4,justify='right').grid(row=2,column=1)

lpav= Label(font=('arial', 16, 'bold'),text="pav bhaji",bd=16,anchor="w").grid(row=3, column=0)
epav=Entry(font=('arial',16,'bold'),textvariable=pav,bd=10,insertwidth=4,justify='right').grid(row=3,column=1)

lburger= Label(font=('arial', 16, 'bold'),text="burger",bd=16,anchor="w").grid(row=4, column=0)
eburger=Entry(font=('arial',16,'bold'),textvariable=burger,bd=10,insertwidth=4,justify='right').grid(row=4,column=1)

lchapati= Label(font=('arial', 16, 'bold'),text="chapati makhani",bd=16,anchor="w").grid(row=5, column=0)
echapati=Entry(font=('arial',16,'bold'),textvariable=chapati,bd=10,insertwidth=4,justify='right').grid(row=5,column=1)

ltaco= Label(font=('arial', 16, 'bold'),text="taco",bd=16,anchor="w").grid(row=6, column=0)
etaco=Entry(font=('arial',16,'bold'),textvariable=taco,bd=10,insertwidth=4,justify='right').grid(row=6,column=1)


btotal= Button(font=('arial', 16, 'bold'),text="total",padx=5,pady=10,anchor="w",command=store).grid(row=7, column=0)
bexit=Button(font=('arial',16,'bold'),text="rexit",padx=5,pady=10,command=rexit).grid(row=7,column=1)

root.mainloop()
