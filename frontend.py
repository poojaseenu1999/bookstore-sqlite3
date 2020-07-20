from tkinter import*

app=Tk()
app.title("bookstore")
text_Input1=StringVar()
text_Input2=StringVar()
text_Input3=StringVar()
text_Input4=StringVar()


label1 = Label(app,text="BOOK").grid(row=0,column=0)
label2 = Label(app,text="AUTHOR").grid(row=0,column=2)
label3 = Label(app,text="TITLE").grid(row=1,column=0)
label4 = Label(app,text="ISBN").grid(row=1,column=2)

txt1= Entry(app,textvariable=text_Input1).grid(row=0,column=1)
txt2= Entry(app,textvariable=text_Input2).grid(row=0,column=3)
txt3= Entry(app,textvariable=text_Input3).grid(row=1,column=1)
txt4= Entry(app,textvariable=text_Input4).grid(row=1,column=3)

list1=Listbox(app,height=15,width=35).grid(rowspan=7,columnspan=2)
btn1=Button(app,bg="light blue",text='VIEW ALL',width=14).grid(row=2,column=3)
btn2=Button(app,bg="light blue",text='SEARCH',width=14).grid(row=3,column=3)
btn3=Button(app,bg="light blue",text='ADD ENTRY',width=14).grid(row=4,column=3)
btn4=Button(app,bg="light blue",text='UPDATE SELECTED',width=14).grid(row=5,column=3)
btn5=Button(app,bg="light blue",text='DELETE SELECTED',width=14).grid(row=6,column=3)
btn6=Button(app,bg="light blue",text='CLOSE',width=14).grid(row=7,column=3)



app.mainloop()
