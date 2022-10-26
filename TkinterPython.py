from tkinter import *
# import tkinter.messagebox
# from tkinter.colorchooser import *
# from tkinter.filedialog import *
# from tkinter import ttk


# root = Tk()
# # title  
# root.title('My program')
# # ตำแหน่ง ขนาด จอ 1 
# root.geometry('1500x900+200+10')

# # จอ 2
# root2 = Tk()
# # title  
# root2.title('จอ 2')
# # ตำแหน่ง ขนาด จอ 1 
# root2.geometry('100x100')


# ใส่ข้อความในหน้าจอ
# myLabel1 = Label(text = 'hello world', fg = 'red', font =20, bg ='yellow').place(x=100, y=0)
# myLabel2 = Label(text = 'hi', fg = 'red', font =20, bg ='yellow', padx=35, pady=15).pack()  # ถ้าใช้ grid ไม่สามารถใช้ pack() ได้
# myLabel3 = Label(text = 'hello world', fg = 'black', font =20, bg ='#B3FFAE').grid(row=5, column=0)

# def showMessage(): 
#     message = txt.get()
#     myLabel1 = Label(text = message, fg = 'red', font =20, bg ='yellow').pack()

# #ใส่ปุ่ม >>>>
# # btn1 = Button(root, text='บันทึก', fg='white', bg = 'red').grid(row=1,column=0)
# btn2 = Button(root, text='บันทึก', fg='white', bg = 'red', command=showMessage).pack()# เรียกใช้งาน function 

# # กล่องข้อความ >>>
# txt=StringVar()
# myText=Entry(root, textvariable=txt).pack()

# def test1():
#     tkinter.messagebox.showinfo('error1','this is my program')
# def exitProgram(): 
#     confirm = tkinter.messagebox.askquestion('ยืนยัน','ต้องการปิดโปรแกรมหรือไม่')
#     if confirm == 'yes':
#         root.destroy() # close program


# # สร้าง menu >>>
# myMenu = Menu()
# root.config(menu=myMenu)
# # menu item >>>
# menuitem = Menu()
# menuitem.add_command(label='item1', command=test1)
# menuitem.add_command(label='item2', command=exitProgram)
# menuitem.add_command(label='item3')
# menuitem.add_command(label='item4')
# # main menu >>>>
# myMenu.add_cascade(label='menu1', menu=menuitem)
# myMenu.add_cascade(label='menu2')
# myMenu.add_cascade(label='menu3')


# def selectColor(): 
#     color = askcolor()
#     print(color)

# def selectFile():
#     # fileopen = askopenfile()
#     fileopen = askopenfilename() 
#     filetxt = open(fileopen, encoding='utf-8')
#     myLabel = Label(text=filetxt.read()).pack()

# button1 = Button(text='select color', command=selectColor).pack()
# button2 = Button(text='select file', command=selectFile).pack()

# def showChoose():
#     choose = language.get()
#     print(choose)

# # เพิ่ม choose >>>>>>
# language = IntVar() 
# language.set(2)
# Radiobutton(text='Python',variable=language, value=1, command=showChoose).grid(row=0,column=0) 
# Radiobutton(text='java',variable=language, value=2, command=showChoose).grid(row=0,column=1) 
# Radiobutton(text='C#',variable=language, value=3, command=showChoose).grid(row=0,column=2) 
# Radiobutton(text='php',variable=language, value=4, command=showChoose).grid(row=0,column=3) 

# checkbox >>>>>>>>>>>>>>>>> 1,0
# def showChoice():
#     print(language1.get())
#     print(language2.get())
#     print(language3.get())
#     print(language4.get())

# language1 = IntVar()
# Checkbutton(text='python',variable=language1).pack(anchor=W) # .pack(anchor = w) คือการกำหนดทิศทาง
# language2 = IntVar()
# Checkbutton(text='jave',variable=language2).pack(anchor=W) # .pack(anchor = w) คือการกำหนดทิศทาง
# language3 = IntVar()
# Checkbutton(text='c',variable=language3).pack(anchor=W) # .pack(anchor = w) คือการกำหนดทิศทาง
# language4 = IntVar()
# Checkbutton(text='php',variable=language4).pack(anchor=W) # .pack(anchor = w) คือการกำหนดทิศทาง
# Button(text='แสดงตัวเลือก', command=showChoice).pack(anchor=W)


# # entry box >>>>>>>

# Label(text='name').grid(row=0)
# Label(text='lastname').grid(row=1)
# Label(text='tel').grid(row=2)

# et1=Entry()
# et1.grid(row=0, column=1)
# et1.insert(0, 'jiraphon')
# et2=Entry()
# et2.grid(row=1,column=1)
# et3=Entry()
# et3.grid(row=2,column=1)

# def deleteText() : 
#     et1.delete(0, END)
#     et2.delete(0, END)
#     et3.delete(0, END)
# button1 = Button(text='clear', command=deleteText).grid(row=3, column=1)



# Combobox >>>>
# Label(text='ที่อยู่', font=20).grid(row=0, column=0)

# choice = StringVar(value='เลือกจังหวัดของคุณ')
# combo = ttk.Combobox(textvariable=choice)
# combo['values'] = ("test1", "test2", "test3")
# combo.grid(row=0, column=1)
# def test01(): 
#     Label(text='คุณเลือก : '+choice.get(), font=20).grid(row=2,column=1)
# button1 = Button(text='ส่งข้อมูล', command=test01).grid(row=1, column=1)



# รับค่าผ่าน keyboard 
root = Tk()
root.geometry("615x400") 
def my_callback(event):
    # l1.config(text='Clicked the key : '+ event.char)
    l1.config(text='Clicked the key : '+ event.keysym)

l1=Label(root,text='to Display',bg='yellow',font=('Times',26,'normal'))
l1.grid(row=0,column=1,padx=10,pady=10)

root.bind('<Key>',my_callback) # Key a is pressed
root.bind('<K>',my_callback) # Key K is pressed


root.mainloop()


