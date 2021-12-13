from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
klik=0
a=["а","и","с","ъ"] #1
b=["б","й","т","ы"] #2
c=["в","к","у","ь"] #3
d=["г","л","ф","э"] #4
e=["д","м","х","ю"] #5
f=["е","н","ц","я"] #6
g=["ё","о","ч"]     #7
h=["ж","п","ш"]     #8
i=["з","р","щ"]     #9
j=[]
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
    x=ent.get()
    x=list(x)
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
        elif y in f:
            j.append(6)
        elif y in g:
            j.append(7)
        elif y in h:
            j.append(8)
        elif y in i:
            j.append(9)
        
        l=sum(j)
        #l=list(str(l))
        v=map(int, str(l))
        l=sum(v)

        lbl_result.configure(text="Число вашего имени: "+str(l))

aken=Tk()
aken.title("akna nimetus")
aken.geometry("1920x1080")
def uus_aken(ind:int):
    if askyesno("Küsimus","Kas teen lahti?"):
        showinfo("Vastus","Teen lahti aken")
    else:
        aken.destroy()
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["snake1.gif","1.gif","2.gif","3.gif"]

ent=Entry(aken,fg="blue",width=20,font="Arial 20")
lbl=Label(aken,text="Sisestage oma nimi palun!")
btn=Button(aken,text="arvuta nimi numbri",font="Arial 20",fg="green",bg="lightblue",height=1)
lbl_result=Label(aken,text="Arvutuse resultaat:",bg="white",height=4,width=20,font="Arial 20")
btn.bind("<Button-1>",nimi_arvutamine)



lbl.pack()
ent.pack()
btn.pack()
lbl_result.pack()


aken.mainloop()