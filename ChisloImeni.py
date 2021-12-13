from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.scrolledtext import *
klik=0
a=["а","и","с","ъ"] #1
b=["б","й","т","ы"] #2  
c=["в","к","у","ь"] #3
d=["г","л","ф","э"] #4
e=["д","м","х","ю"] #5
f1=["е","н","ц","я"]#6
g=["ё","о","ч"]     #7
h=["ж","п","ш"]     #8
i=["з","р","щ"]     #9
a1=["a","i","s"]    #1
b1=["b","t","q"]    #2  
c1=["v","k","u"]    #3
d1=["g","l","f"]    #4
e1=["d","m","h","y"]#5
f11=["e","n"]       #6
g1=["o"]            #7
h1=["p"]            #8
i1=["z","r"]        #9
j=[]
def uus_aken(ind:int):
    if askyesno("Küsimus","Kas teen lahti?"):
        showinfo("Vastus","Teen lahti aken")
    else:
        aken.destroy()
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["snake1.gif","1.gif","2.gif","3.gif"]
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)

def klikker1(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)
    
def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)

def nimi_arvutamine(event):
    l=0
    x=ent.get().lower()
    x=list(x)
    j=[]
    for y in x:
        if y in a:
            j.append(1)
        elif y in b:
            j.append(2)
        elif y in c:
            j.append(3)
        elif y in d:
            j.append(4)
        elif y in e:
            j.append(5)
        elif y in f1:
            j.append(6)
        elif y in g:
            j.append(7)
        elif y in h:
            j.append(8)
        elif y in i:
            j.append(9)
        
        l=sum(j)
        v=map(int, str(l))
        l=sum(v)
        data = []
        if l==1:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 1
                b1 = 8
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==2:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 10
                b1 = 16
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==3:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 18
                b1 = 23
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==4:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 25
                b1 = 30
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==5:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 32
                b1 = 39
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==6:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 41
                b1 = 46
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==7:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 48
                b1 = 54
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==8:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 56
                b1 = 62
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        elif l==9:
            with open("TextFile1.txt","r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                a1 = 64
                b1 = 68
                p=("\n".join(lines[a1:b1]))
                lbl_result.configure(text="Число вашего имени: "+str(l)+"\n"+str(p))
        else:
            lbl_result.configure(text="К сожалению число вашего имени не имеет значения в базе данных")


aken=Tk()
aken.title("ЧИСЛО ИМЕНИ")
aken.geometry("1920x1080")




ent=Entry(aken,fg="blue",width=20,font="Arial 20")
lbl=Label(aken,text="Sisestage oma nimi palun!")
btn=Button(aken,text="arvuta nimi numbri",font="Arial 20",fg="green",bg="lightblue",height=1)
lbl_result=Label(aken,text="Расчеты имени",bg="white",font="Arial 20",borderwidth=50,wraplength=1920)

btn.bind("<Button-1>",nimi_arvutamine)


lbl.pack()
ent.pack()
btn.pack()
lbl_result.pack()
aken.mainloop()