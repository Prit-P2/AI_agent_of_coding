import tkinter as tk
from tkinter import ttk
def click():
    a=value.get()
    b=a.casefold()
    if b=="what is tkinter":
        f1=tk.Frame(f3)
        tk.Label(root,text="It is a python biuilt module that can used to make gui").pack(side=tk.LEFT)
    elif b=="slider":
        f1=tk.Frame(f3)
        f="""To create a slider
        we can use scale wedget
         Exmple"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
slider=tk.Slider(root,form_=0,to=100,orient=HORIZANTAL,tickinterval=50 )"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="messagebox":
        f1=tk.Frame(f3)
        f="""To open  messagebox
        we need to import messagebox
         Exmple"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
import tkinter.messagebox as tmsg
tmsg.showinfo("title","Message")"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="image" or b=="how to open .jpg image":
        f1=tk.Frame(f3)
        f="""To open .jpg or any other 
        kind of image 
         Exmple"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
form PIL import imageTk,image"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="variable" or b=="how to create variable":
        f1=tk.Frame(f3)
        f="""To create a variable
        in tkinter we can define it normally but
        string or int 
         Exmple"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
any_variable=tkinter.StringVar
# .BooleanVar or .DoubleVar or .IntVar or .StringVar for any operation"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    elif b==".get" or b=="how to take value form variable":
        f1=tk.Frame(f3)
        f="""To take value from variable 
         we use .get comand to take out value 
         Exmple"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
any_variable.get()"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    elif b==".set" or b=="how to set value":
        f1=tk.Frame(f3)
        f="""To set value we use .set 
        comand to set valaue
        Exmple"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
any_variable.set("value")
#""-if it is string other don't use"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    # to print any text in tkinter
    elif b=="how to print text":
        f1=tk.Frame(f3)
        f="""To print text in tkinter GUI we can
         use Label to print text """
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""Exmple
tkinter.Label(root,text="anytext")"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="label":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to print tet in the GUI",font=("",15)).pack()
        code="""tkinter.Label(root,text="anytext")"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack(side=tk.LEFT)
        prompet.delete(0,tk.END)
        f1.pack()
    # Frame    
    elif b=="frame":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to make fram in the GUI",font=("",15)).pack()
        code="""Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    # to take enntry from user
    elif b=="how to take value from user" or b=="how to take entery":
        f1=tk.Frame(f3)
        f="""to take value from user or to take entery
        we need to use entery wegit of tkinter"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""var=tkinter.StringVar()
tkinter.Entry(root,textvariable=var,font=("",20))"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="entry":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to take value  in the GUI",font=("",15)).pack()
        code="""var=tkinter.StringVar()
tkinter.Entry(root,textvariable=var,font=("",20))"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    # how to use tkinter GUI writing as notpad
    elif b=="how to create text editor writing":
        f1=tk.Frame(f3)
        f="""to create  a text editor writing we can use wegit text"""
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""tkinter.Text(root).pack(fill="both")"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="text":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to write like a letter or note and many more in the GUI",font=("",15)).pack()
        code="""tkinter.Text(root).pack(fill="both")"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    # creat radio button

    elif b=="how to create radiobutton":
        f1=tk.Frame(f3)
        f="""to create a radio button we 
         can use radiobutton wegite """
        ttk.Label(f1,text=f,font=("",15)).pack()
        code="""
var=tk.StringVar()
radio=tk.Radiobutton(root,text="Hello",variable=var,value="Dhoa").pack()
radio=tk.Radiobutton(root,text="Hmrmh",variable=var,value="magi").pack()
radio=tk.Radiobutton(root,text="Hellorhg",variable=var,value="fghg").pack()
radio=tk.Radiobutton(root,text="Hellorh",variable=var,value="ghf").pack()
root.mainloop()"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="radiobutton":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to make radio button that can check only one cheack marke  in the GUI",font=("",15)).pack()
        code="""
var=tk.StringVar()
radio=tk.Radiobutton(root,text="Hello",variable=var,value="Dhoa").pack()
radio=tk.Radiobutton(root,text="Hmrmh",variable=var,value="magi").pack()
radio=tk.Radiobutton(root,text="Hellorhg",variable=var,value="fghg").pack()
radio=tk.Radiobutton(root,text="Hellorh",variable=var,value="ghf").pack()
root.mainloop()"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="listbox":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to make Listbox  in the GUI",font=("",15)).pack()
        code="""lb=tk.Listbox(root)
lb.pack()
lb.insert("1","Fmfmdfgdfmg")"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="canvas":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to make canves and drowing tools to make GUI attractive",font=("",15)).pack()
        code="""cn=tk.Canvas(root,height=400,width=600,bg="#CCFFFF")
cn.create_rectangle(100,100,500,300,fill="#66FFFF") # 1th and 2nd is starting point and 3th and 4th is ending point
cn.create_line(100,100,500,300) # first and second entry is starting point and third and fourth is ending point
cn.create_line(500,100,100,300) #
cn.pack()"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="manue":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to make manue bar  in the GUI",font=("",15)).pack()
        code="""menu=tk.Menu(root)
addmenu=tk.Menu(menu,tearoff=0)
addmenu.add_command(label="Ne",command=New)
addmenu.add_command(label="save",command=save)
addmenu.add_command(label="open",command=open)
addmenu.add_command(label="quit",command=quit)
menu.add_cascade(label="File",menu=addmenu)
root.config(menu=menu)"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",15),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    elif b=="scrollbar":
        f1=tk.Frame(f3)
        tk.Label(f1,text="It  is uaed to make scrollbar in the GUI",font=("",15)).pack()
        code="""
        l=Listbox(root,yscrollcommand=scrollbar.set)
l.insert(1,"jpjyr")
l.insert(2,"trjffgj")
l.insert(3,"trjffgj")
l.insert(4,"trjffgj")
l.insert(5,"trjffgj")
l.insert(6,"trjffgj")
l.insert(7,"trjffgj")
l.insert(8,"trjffgj")
l.insert(9,"trjffgj")
l.insert(10,"trjffgj")
l.insert(11,"trjffgj")

l.pack()
scrollbar.config(command=l.yview)"""
        def copy():
            root.clipboard_clear()
            root.clipboard_append(code)
            root.update()
        ttk.Label(f1,text=code,font=("Courier",12),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        code="""# to create it in whole root body we can use to method fisrt is Text wegit
        # and other is canvas frame method i.e shown:
        # Maain  frame creation
frame=tk.Frame(root)
frame.pack(fill="both",expand=1)
# creating a canvas
c=tk.Canvas(frame)
c.pack(side="left",fill="both",expand=1)
# create a scrollbar
bar=ttk.Scrollbar(frame,orient="vertical",command=c.yview)
bar.pack(side="right",fill="y")
bar1=ttk.Scrollbar(frame,orient="horizontal",command=c.xview)
bar1.pack(side="bottom",fill="x")
# configer the canvas
c.config(yscrollcommand=bar.set)
c.bind('<Configure>',lambda e:c.config(scrollregion=c.bbox("all")))
c.config(xscrollcommand=bar1.set)
c.bind('<Configure>',lambda e:c.config(scrollregion=c.bbox("all")))
# create another frame
f3=tk.Frame(c)
# add that new frame to window in a canvas
c.create_window((0,0),window=f3,anchor="nw")

f=tk.Frame(f3)
h=tk.Label(f3,text="Hello,wthat can I help you about tkinter",font=("",10),bg="#fbc293").pack()"""
        ttk.Label(f1,text=code,font=("Courier",12),background="black",foreground="white",justify="left").pack(padx=10,pady=10,side=tk.LEFT)
        coppy=ttk.Button(f1,text="coppy",command=copy).pack()
        prompet.delete(0,tk.END)
        f1.pack()
    else:
        f1=tk.Frame(f3)
        ttk.Label(f1,text="SyantexError").pack()
        prompet.delete(0,tk.END)
        f1.pack()
    
root=tk.Tk()
root.geometry("500x400")
# root.minsize(500,400)
# root.maxsize(500,400)
value=tk.StringVar()
# Maain  frame creation
frame=tk.Frame(root)
frame.pack(fill="both",expand=1)
# creating a canvas
c=tk.Canvas(frame)
c.pack(side="left",fill="both",expand=1)
# create a scrollbar
bar=ttk.Scrollbar(frame,orient="vertical",command=c.yview)
bar.pack(side="right",fill="y")
bar1=ttk.Scrollbar(frame,orient="horizontal",command=c.xview)
bar1.pack(side="bottom",fill="x")
# configer the canvas
c.config(yscrollcommand=bar.set)
c.bind('<Configure>',lambda e:c.config(scrollregion=c.bbox("all")))
c.config(xscrollcommand=bar1.set)
c.bind('<Configure>',lambda e:c.config(scrollregion=c.bbox("all")))
# create another frame
f3=tk.Frame(c)
# add that new frame to window in a canvas
c.create_window((0,0),window=f3,anchor="nw")

f=tk.Frame(f3)
h=tk.Label(f3,text="Hello,wthat can I help you about tkinter",font=("",10),bg="#fbc293").pack()
prompet=tk.Entry(f,textvariable=value,font=("",20),bg="#b6ecf4")
prompet.pack(fill="x")
tk.Button(f,text="<>",command=click,font=("",15),bg="blue",fg="white").pack(side=tk.RIGHT)
f.pack(side=tk.BOTTOM,fill="x")
root.mainloop()
