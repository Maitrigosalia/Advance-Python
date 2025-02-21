from tkinter import *
from tkinter import messagebox 
import time 
import FastFood as f
import SabziRoti as s

def mainmenu():
    def exit():
        root.destroy()

    def sr():
        exit()
        s.sabziroti()
    def ff():
        exit()
        f.fastfood()

    root=Tk()
    root.title("Urban Chawk")
    root.geometry("1920x1080")
    root.attributes("-fullscreen",True)
    Tops=Frame(root)
    Tops.pack(side=TOP)
    mains=Frame(root)
    mains.pack()
    
    localtime=time.asctime(time.localtime(time.time()))
    lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="Urban Chawk",fg="Black",bd=10,anchor='w')
    lblInfo.grid(row=0,column=0)
    lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime)
    lblInfo.grid(row=0,column=3)

    btn2=Button(mains,text="FastFood",command=ff)
    btn2.grid(row=6,column=3)
    btn2=Button(mains,text="SabziRoti",command=sr)
    btn2.grid(row=8,column=3)
    btn2=Button(mains,text="Exit",command=exit)
    btn2.grid(row=10,column=5)
    root.mainloop()


if __name__=="__main__":
    mainmenu()