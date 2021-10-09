import tkinter as tk;
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *

def Getvalue(event):
    e1.delete(0,END) #clearing all the stuff
    e2.delete(0,END)
    e3.delete(0,END)
    row_id = listBox.selection()[0]  #get the values from the list box
    select = listBox.set(row_id)
    e1.insert(0,select['id'])  #assigning to the text field
    e2.insert(0,select['name'])
    e3.insert(0,select['eventtype'])

def Add():
    personid=e1.get();  #storing inputs
    personname=e2.get()
    event_type=e3.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="details")
    mycursor=mysqldb.cursor()

    try:
        sql="INSERT INTO detail (id,name,eventtype) VALUES (%s,%s,%s)"
        val=(personid,personname,event_type)
        mycursor.execute(sql,val)
        mysqldb.commit()
    
        messagebox.showinfo("information","record inserted successfully")
        e1.delete(0,END)  #clearing text fields
        e2.delete(0,END)
        e3.delete(0,END)


    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    personid=e1.get()
    personname=e2.get()
    event_type=e3.get()


    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="details")
    mycursor=mysqldb.cursor()

    try:
        sql="update detail set name=%s,eventtype=%s where id=%s"
        val=(personname,event_type,personid)
        mycursor.execute(sql,val)
        mysqldb.commit()

        messagebox.showinfo("information","record updated successfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
     personid=e1.get()

     mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="details")
     mycursor=mysqldb.cursor()

     try:
         sql="delete from detail where id=%s"
         val=(personid,)
         mycursor.execute(sql,val)
         mysqldb.commit()
        
         messagebox.showinfo("information","record deleted successfully")
         e1.delete(0,END)
         e2.delete(0,END)
         e3.delete(0,END)
     except Exception as e:
         print(e)
         mysqldb.rollback()
         mysqldb.close()


def eventbyname():
    global name
    name1=e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="details")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT * FROM detail where eventtype=%s",(name1,))
    for i in mycursor:
        print(i)

def eventbyperson():
    global name2
    name2=e5.get()
    
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="details")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT * FROM detail where name=%s",(name2,))
    for i in mycursor:
        print(i)




#showing details on gui (list)
def show():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="details")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT id,name,eventtype FROM detail")
    records=mycursor.fetchall()
    print(records)


    for i,(id,pname,event) in enumerate(records,start=1): #loop and put it on to listBox
        listBox.insert("","end",values=(id,pname,event))
        mysqldb.close()

root=Tk()
root.geometry('800x500')
global e1
global e2
global e3
global e4
global e5

tk.Label(root,text="Event Management" , fg="red", font=(None,30)).place(x=300,y=5) #name

tk.Label(root,text="Person ID").place(x=10,y=10)  #labels
Label(root,text="Person Name").place(x=10,y=40)
Label(root,text="Event Type").place(x=10,y=70)

Label(root,text='Search_by_event').place(x=10,y=100)
Label(root,text="Search_by_name").place(x=400,y=100)


e1=Entry(root) #textfield positions
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)

e3=Entry(root)
e3.place(x=140,y=70)

e4=Entry(root)
e4.place(x=140,y=100)

e5=Entry(root)
e5.place(x=550,y=100)

Button(root,text="Add",command=Add,height=3,width=13).place(x=30,y=130)  #buttons dd,update,delete
Button(root,text="update",command=update,height=3,width=13).place(x=140,y=130)
Button(root,text="Delete",command=delete,height=3,width=13).place(x=250,y=130)
Button(root,text="searchbyevent",command=eventbyname,height=3,width=13).place(x=360,y=130)
Button(root,text="searchbyname",command=eventbyperson,height=3,width=13).place(x=490,y=130)


cols=('id','name','eventtype') #columns display on gui
listBox =ttk.Treeview(root,columns=cols,show='headings')

for col in cols:
    listBox.heading(col,text=col) 
    listBox.grid(row=1,column=0,columnspan=2)
    listBox.place(x=10,y=200)

show()
listBox.bind('<Double-Button-1>',Getvalue)
root.mainloop()
