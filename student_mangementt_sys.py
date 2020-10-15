# Functions:
def add_student():
    def submit_add_data():
        id= id_value.get()
        name= name_value.get()
        mobile= mobile_value.get()
        email= email_value.get()
        address=address_value.get()
        gender=gender_value.get()
        dob=dob_value.get()
        added_date=time.strftime('%d/%m/%Y')
        added_time=time.strftime("%H:%M:%S")

        try:
            query='insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(id,name,mobile,email,address,gender,dob,added_date,added_time))
            con.commit()
            message=messagebox.askyesnocancel('Notification','Id {} Name {} Added successfully...and want to clean the form'.format(id,name),parent=addroot)
            if(message==True):
                id_value.set('')
                name_value.set('')
                mobile_value.set('')
                email_value.set('')
                address_value.set('')
                gender_value.set('')
                dob_value.set('')
        except:
            messagebox.showerror('Notification','ID already exists',parent=addroot)
        query='select * from Student'
        mycursor.execute(query)
        data=mycursor.fetchall()
        #tree_view.delete(*tree_view.get_children()) # delete all from tree_view frame
        #for i in data:
            #tree_view_data=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            #tree_view.insert('',END,values=tree_view_data)

    addroot=Toplevel(master=data_entry_frame) # opens TPL window in that frame only
    addroot.geometry('470x450+220+200')

    addroot.config(bg='blue')

    addroot.grab_set()  # no other windows will pop up and no button will be clicked other than top-level window
    addroot.iconbitmap('student_management.ico')
    addroot.resizable(False, False)

    id_label=Label(addroot,text='Enter ID',anchor='w',font=('times',15,'bold'),width=13)
    name_label = Label(addroot, text='Enter name',anchor='w',font=('times',15,'bold'),width=13)
    mobile_label = Label(addroot, text='Enter Mobile no',anchor='w',font=('times',15,'bold'),width=13)
    email_label = Label(addroot, text='Enter email',anchor='w',font=('times',15,'bold'),width=13)
    address_label = Label(addroot, text='Enter address',anchor='w',font=('times',15,'bold'),width=13)
    gender_label = Label(addroot, text='Enter Gender',anchor='w',font=('times',15,'bold'),width=13)
    dob_label = Label(addroot, text='Enter DOB',anchor='w',font=('times',15,'bold'),width=13)

    id_label.place(x=10,y=10)
    name_label.place(x=10,y=60)
    mobile_label.place(x=10,y=110)
    email_label.place(x=10,y=160)
    address_label.place(x=10,y=210)
    gender_label.place(x=10,y=260)
    dob_label.place(x=10,y=310)

    id_value = StringVar()
    name_value = StringVar()
    mobile_value = StringVar()
    email_value = StringVar()
    address_value = StringVar()
    gender_value = StringVar()
    dob_value = StringVar()

    id_details = Entry(addroot, textvariable=id_value, borderwidth=5,width=30)
    name_details = Entry(addroot, textvariable=name_value, borderwidth=5, width=30)
    mobile_details = Entry(addroot, textvariable=mobile_value, borderwidth=5, width=30)
    email_details = Entry(addroot, textvariable=email_value, borderwidth=5, width=30)
    address_details = Entry(addroot, textvariable=address_value, borderwidth=5, width=30)
    gender_details = Entry(addroot, textvariable=gender_value, borderwidth=5, width=30)
    dob_details = Entry(addroot, textvariable=dob_value, borderwidth=5, width=30)

    id_details.place(x=230, y=10,height=30)
    name_details.place(x=230, y=60, height=30)
    mobile_details.place(x=230, y=110, height=30)
    email_details.place(x=230, y=160, height=30)
    address_details.place(x=230, y=210, height=30)
    gender_details.place(x=230, y=260, height=30)
    dob_details.place(x=230, y=310, height=30)

    add_button=Button(addroot,text='ADD',width=10,activebackground='green',font=('times',13,'bold'),command=submit_add_data)
    add_button.place(x=160,y=400)

    addroot.mainloop()

def search_student():

    def search():
        id = id_value.get()
        name = name_value.get()
        mobile = mobile_value.get()
        email = email_value.get()
        address = address_value.get()
        gender = gender_value.get()
        dob = dob_value.get()
        added_date = time.strftime('%d/%m/%Y')

        if id!='':
            query='select * from Student where id=%s'
            mycursor.execute(query,(id))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif name!='':
            query='select * from Student where name=%s'
            mycursor.execute(query,(name))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif mobile!='':
            query='select * from Student where mobile=%s'
            mycursor.execute(query,(mobile))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif email!='':
            query='select * from Student where email=%s'
            mycursor.execute(query,(email))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif address!='':
            query='select * from Student where address=%s'
            mycursor.execute(query,(address))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif gender!='':
            query='select * from Student where gender=%s'
            mycursor.execute(query,(gender))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif dob!='':
            query='select * from Student where dob=%s'
            mycursor.execute(query,(dob))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

        elif added_date!='':
            query='select * from Student where added_date=%s'
            mycursor.execute(query,(added_date))
            data=mycursor.fetchall()
            tree_view.delete(*tree_view.get_children())
            for i in data:
                tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                tree_view.insert('', END, values=tree_view_data)

    searchroot = Toplevel(master=data_entry_frame)  # opens TPL window in that frame only
    searchroot.geometry('470x470+220+200')

    searchroot.config(bg='blue')

    searchroot.grab_set()  # no other windows will pop up and no button will be clicked other than top-level window
    searchroot.iconbitmap('student_management.ico')
    searchroot.resizable(False, False)

    id_label = Label(searchroot, text='Enter ID', anchor='w', font=('times', 15, 'bold'), width=13)
    name_label = Label(searchroot, text='Enter name', anchor='w', font=('times', 15, 'bold'), width=13)
    mobile_label = Label(searchroot, text='Enter Mobile no', anchor='w', font=('times', 15, 'bold'), width=13)
    email_label = Label(searchroot, text='Enter email', anchor='w', font=('times', 15, 'bold'), width=13)
    address_label = Label(searchroot, text='Enter address', anchor='w', font=('times', 15, 'bold'), width=13)
    gender_label = Label(searchroot, text='Enter Gender', anchor='w', font=('times', 15, 'bold'), width=13)
    dob_label = Label(searchroot, text='Enter DOB',anchor='w', font=('times', 15, 'bold'), width=13)
    date_label = Label(searchroot, text='Enter Date', anchor='w', font=('times', 15, 'bold'), width=13)

    id_label.place(x=10, y=10)
    name_label.place(x=10, y=60)
    mobile_label.place(x=10, y=110)
    email_label.place(x=10, y=160)
    address_label.place(x=10, y=210)
    gender_label.place(x=10, y=260)
    dob_label.place(x=10, y=310)
    date_label.place(x=10, y=360)

    id_value=StringVar()
    name_value = StringVar()
    mobile_value = StringVar()
    email_value = StringVar()
    address_value = StringVar()
    gender_value = StringVar()
    dob_value = StringVar()
    date_value = StringVar()


    id_details = Entry(searchroot, textvariable=id_value, borderwidth=5, width=30)
    name_details = Entry(searchroot, textvariable=name_value, borderwidth=5, width=30)
    mobile_details = Entry(searchroot, textvariable=mobile_value, borderwidth=5, width=30)
    email_details = Entry(searchroot, textvariable=email_value, borderwidth=5, width=30)
    address_details = Entry(searchroot, textvariable=address_value, borderwidth=5, width=30)
    gender_details = Entry(searchroot, textvariable=gender_value, borderwidth=5, width=30)
    dob_details = Entry(searchroot, textvariable=dob_value, borderwidth=5, width=30)
    date_details = Entry(searchroot, textvariable=date_value, borderwidth=5, width=30)

    id_details.place(x=230, y=10, height=30)
    name_details.place(x=230, y=60, height=30)
    mobile_details.place(x=230, y=110, height=30)
    email_details.place(x=230, y=160, height=30)
    address_details.place(x=230, y=210, height=30)
    gender_details.place(x=230, y=260, height=30)
    dob_details.place(x=230, y=310, height=30)
    date_details.place(x=230, y=360, height=30)

    search_button = Button(searchroot, text='SEARCH', width=10, activebackground='green',font=('times',13,'bold'),command=search)
    search_button.place(x=170, y=420)

    searchroot.mainloop()

def delete_student():
    click=tree_view.focus() #
    content=tree_view.item(click)
    index=content['values'][0]
    query='delete from Student where id=%s'
    mycursor.execute(query,(index))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully'.format(index))
    query = 'select * from Student'
    mycursor.execute(query)
    data = mycursor.fetchall()
    tree_view.delete(*tree_view.get_children())
    for i in data:
        tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        tree_view.insert('', END, values=tree_view_data)

def update_student():

    def update_submit():
        id = id_value.get()
        name = name_value.get()
        mobile = mobile_value.get()
        email = email_value.get()
        address = address_value.get()
        gender = gender_value.get()
        dob = dob_value.get()
        date = date_value.get()
        time=time_value.get()

        query='update Student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('notification','Id {} modified successfully....'.format(id),parent=update_submit())
        query = 'select * from Student'
        mycursor.execute(query)
        data = mycursor.fetchall()
        tree_view.delete(*tree_view.get_children())
        for i in data:
            tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            tree_view.insert('', END, values=tree_view_data)


    updateroot = Toplevel(master=data_entry_frame)  # opens TPL window in that frame only
    updateroot.geometry('470x500+220+200')

    updateroot.config(bg='blue')

    updateroot.grab_set()  # no other windows will pop up and no button will be clicked other than top-level window
    updateroot.iconbitmap('student_management.ico')
    updateroot.resizable(False, False)

    id_label = Label(updateroot, text='Enter ID', anchor='w', font=('times', 15, 'bold'), width=13)
    name_label = Label(updateroot, text='Enter name', anchor='w', font=('times', 15, 'bold'), width=13)
    mobile_label = Label(updateroot, text='Enter Mobile no', anchor='w', font=('times', 15, 'bold'), width=13)
    email_label = Label(updateroot, text='Enter email', anchor='w', font=('times', 15, 'bold'), width=13)
    address_label = Label(updateroot, text='Enter address', anchor='w', font=('times', 15, 'bold'), width=13)
    gender_label = Label(updateroot, text='Enter Gender', anchor='w', font=('times', 15, 'bold'), width=13)
    dob_label = Label(updateroot, text='Enter DOB', anchor='w', font=('times', 15, 'bold'), width=13)
    date_label = Label(updateroot, text='Enter Date', anchor='w', font=('times', 15, 'bold'), width=13)
    time_label = Label(updateroot, text='Enter Time', anchor='w', font=('times', 15, 'bold'), width=13)

    id_label.place(x=10, y=10)
    name_label.place(x=10, y=60)
    mobile_label.place(x=10, y=110)
    email_label.place(x=10, y=160)
    address_label.place(x=10, y=210)
    gender_label.place(x=10, y=260)
    dob_label.place(x=10, y=310)
    date_label.place(x=10, y=360)
    time_label.place(x=10,y=410)

    id_value = StringVar()
    name_value = StringVar()
    mobile_value = StringVar()
    email_value = StringVar()
    address_value = StringVar()
    gender_value = StringVar()
    dob_value = StringVar()
    date_value = StringVar()
    time_value=StringVar()

    id_details = Entry(updateroot, textvariable=id_value, borderwidth=5, width=30)
    name_details = Entry(updateroot, textvariable=name_value, borderwidth=5, width=30)
    mobile_details = Entry(updateroot, textvariable=mobile_value, borderwidth=5, width=30)
    email_details = Entry(updateroot, textvariable=email_value, borderwidth=5, width=30)
    address_details = Entry(updateroot, textvariable=address_value, borderwidth=5, width=30)
    gender_details = Entry(updateroot, textvariable=gender_value, borderwidth=5, width=30)
    dob_details = Entry(updateroot, textvariable=dob_value, borderwidth=5, width=30)
    date_details = Entry(updateroot, textvariable=date_value, borderwidth=5, width=30)
    time_details= Entry(updateroot, textvariable=time_value, borderwidth=5, width=30)

    id_details.place(x=230, y=10, height=30)
    name_details.place(x=230, y=60, height=30)
    mobile_details.place(x=230, y=110, height=30)
    email_details.place(x=230, y=160, height=30)
    address_details.place(x=230, y=210, height=30)
    gender_details.place(x=230, y=260, height=30)
    dob_details.place(x=230, y=310, height=30)
    date_details.place(x=230, y=360, height=30)
    time_details.place(x=230, y=410, height=30)

    search_button = Button(updateroot, text='UPDATE', width=10, activebackground='green', font=('times', 13, 'bold'),command=update_submit)
    search_button.place(x=150, y=465)

    click=tree_view.focus()
    content=tree_view.item(click)
    index=content['values']

    if (len(index)!=0):
        id_value.set(index[0])
        name_value.set(index[1])
        mobile_value.set(index[2])
        email_value.set(index[3])
        address_value.set(index[4])
        gender_value.set(index[5])
        dob_value.set(index[6])
        date_value.set(index[7])
        time_value.set(index[8])

    updateroot.mainloop()

def show_all():
    query='select * from Student'
    mycursor.execute(query)
    data = mycursor.fetchall()
    tree_view.delete(*tree_view.get_children())  # delete all from tree_view frame
    for i in data:
        tree_view_data = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        tree_view.insert('', END, values=tree_view_data)

def export():
    save_as=filedialog.asksaveasfilename()
    file_data=tree_view.get_children()
    id,name,mobile,email,address,gender,dob,added_date,added_time=[],[],[],[],[],[],[],[],[]
    for i in file_data:
        content=tree_view.item(i)
        
def exit():
    message_box=messagebox.askyesnocancel('Notification','Do you want to Exit?')
    if message_box==True:
        root.destroy()  # closes the main window

def connect_db():

    def submit_db():
        global con,mycursor
        #host=host_value.get()
        #username=username_value.get()
        #password=password_value.get()

        host='localhost'
        username='root'
        password='kaushik9868@'


        # try will be executed if credentials are correct otherwise except will be executed
        try:
            con=pymysql.connect(host=host,user=username,password=password)
            mycursor=con.cursor()

        except:
            messagebox.showerror('Notifications','Data is incorrect,please try again')
            return

        try:
            query='create database Student_Management_System'
            mycursor.execute(query)
            query = 'use Student_Management_System'
            mycursor.execute(query)
            query = 'create table Student(id int,name varchar(20),mobile varchar(15),email varchar(100),address varchar(100),gender varchar(10),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(query)
            query = 'alter table Student modify id int not null'
            mycursor.execute(query)
            query = 'alter table Student add primary key(id)'
            mycursor.execute(query)
            messagebox.showinfo('Notification', 'Database created and now you are connected to Database.......', parent=dbroot)


        except:
            query='use Student_Management_System'
            mycursor.execute(query)
            messagebox.showinfo('Notification','Now you are connected to Database.......',parent=dbroot)
        dbroot.destroy()

    dbroot=Toplevel() # creates top-level window
    dbroot.geometry('500x300+800+200')
    dbroot.grab_set()  # no other windows will pop up and no button will be clicked other than top-level window
    dbroot.iconbitmap('student_management.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='blue')

    host_label= Label(dbroot,text='Enter Host',bg='yellow',width=13,font=('times',12,'bold'),relief=GROOVE,borderwidth=2,anchor='w')
    username_label= Label(dbroot,text='Enter Username',bg='yellow',width=13,font=('times',12,'bold'),relief=GROOVE,borderwidth=2,anchor='w')
    password_label= Label(dbroot,text='Enter Password',bg='yellow',width=13,font=('times',12,'bold'),relief=GROOVE,borderwidth=2,anchor='w')

    host_label.place(x=10,y=10)
    username_label.place(x=10,y=50)
    password_label.place(x=10,y=90)

    host_value=StringVar()
    username_value=StringVar()
    password_value=StringVar()

    host_details = Entry(dbroot, bd=5,textvariable=host_value)
    host_details.place(x=180,y=10)
    username_details= Entry(dbroot,bd=5, textvariable=username_value)
    username_details.place(x=180, y=50)
    password_details = Entry(dbroot,bd=5, textvariable=password_value)
    password_details.place(x=180, y=90)

    submit_button=Button(dbroot,text='Submit',font=('times',15,'bold'),bg='red',command=submit_db)
    submit_button.place(x=200,y=200)


    dbroot.mainloop()








def clock():
    watch=time.strftime('%T')
    date=time.strftime('%d/%m/%Y')
    clock_label.config(text='Date :'+date+"\n"'Time :'+watch)
    clock_label.after(200,clock)

 #---------------------------------------INTRO LABEL
def intro_label():
    global count,text

#------------------------------------------
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
import pymysql
import time
import pandas # to export file in desirable format

root=Tk()
root.title('STUDENT MANAGEMENT SYSTEM') # window heading/title
root.config(bg='grey') # sets window background colour
# every time 'geometry' executes, gives variable window location but to to fix window we use x and y axis
# gives ('width x height + x axis + y axis')
root.geometry('1100x700+200+50') # sets dimension and position of window
# post a picture aside title
root.iconbitmap('student_management.ico') # uses '.ico' format
root.resizable(False,False) # prevents change in window size (width,height)

# FRAMES
data_entry_frame=Frame(root,bg='LIGHT BLUE',relief=GROOVE,borderwidth=3)
data_entry_frame.place(x=10,y=180,width=500,height=500)

data_entry_label=Label(data_entry_frame,text='OPERATIONS',font=('times',20,'bold'),bg='light blue')
data_entry_label.pack(side=TOP,expand=True)

show_data_frame=Frame(root,bg='white',borderwidth=1,relief=GROOVE)
show_data_frame.place(x=520,y=180,width=570,height=500)

scroll_x=Scrollbar(show_data_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(show_data_frame,orient=VERTICAL)
tree_view=Treeview(show_data_frame,columns=('id','name','mobile no.','email','address','gender','dob','added_date','added_time'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tree_view.xview)
scroll_y.config(command=tree_view.yview)
tree_view.heading('id',text='ID')
tree_view.heading('name',text='Name')
tree_view.heading('mobile no.',text='Contact number')
tree_view.heading('email',text='E-Mail')
tree_view.heading('address',text='Address')
tree_view.heading('gender',text='Gender')
tree_view.heading('dob',text='D.O.B')
tree_view.heading('added_date',text='Added Date')
tree_view.heading('added_time',text='Added Time')
tree_view['show']='headings'
tree_view.column('id',width=80)
tree_view.column('name',width=150)
tree_view.column('mobile no.',width=150)
tree_view.column('email',width=200)
tree_view.column('address',width=200)
tree_view.column('gender',width=80)
tree_view.column('dob',width=100)
tree_view.column('added_date',width=100)
tree_view.column('added_time',width=100)
tree_view.pack(fill=BOTH,expand=1)

#---------------------------------------------LABEL-------------------------------#
text='Student Management System'
count=0
slider_label=Label(root,text=text,font=('chiller',20,'italic bold'),relief=SOLID,borderwidth=3,bg='grey',width=30)
slider_label.place(x=390,y=0)

#--------------------------------------------------------------------------------------------------#
clock_label=Label(root,font=('times',15,'italic'),relief=RIDGE,borderwidth=3,bg='grey',width=14)
clock_label.place(x=0,y=0,anchor='nw')
clock()

#show_data_button=Button(root,text='Add',relief=RIDGE,borderwidth=3,width=10)
#show_data_button.place(x=200,y=200)

#------------------------------------ BUTTON----------------

database_button=Button(root,text='Connect to Database',width=30,bg='grey',borderwidth=3,activebackground='blue',activeforeground='white',font=('times',12,'italic'),relief=RIDGE,command=connect_db)
database_button.place(x=800,y=0)

add_student_button=Button(data_entry_frame,text="Add Student",width=25,font=('Arial',12,'italic bold'),relief=RIDGE,bd=9,activebackground='green',command=add_student)
add_student_button.pack(side=TOP,expand=True)

search_student_button=Button(data_entry_frame,text="Search Student",font=('Arial',12,'italic bold'),width=25,relief=RIDGE,borderwidth=9,activebackground='green',command=search_student)
search_student_button.pack(side=TOP,expand=True)

delete_student_button=Button(data_entry_frame,text="Delete Student",font=('Arial',12,'italic bold'),width=25,relief=RIDGE,borderwidth=9,activebackground='green',command=delete_student)
delete_student_button.pack(side=TOP,expand=TRUE)

update_student_button=Button(data_entry_frame,text="Update Student",font=('Arial',12,'italic bold'),width=25,relief=RIDGE,borderwidth=9,activebackground='green',command=update_student)
update_student_button.pack(side=TOP,expand=True)

show_all_button=Button(data_entry_frame,text="Show All",font=('Arial',12,'italic bold'),width=25,relief=RIDGE,borderwidth=9,activebackground='green',command=show_all)
show_all_button.pack(side=TOP,expand=True)

export_student_button=Button(data_entry_frame,text="Export Data",font=('Arial',12,'italic bold'),width=25,relief=RIDGE,borderwidth=9,activebackground='green',command=export)
export_student_button.pack(side=TOP,expand=True)

exit_button=Button(data_entry_frame,text="Exit",font=('Arial',12,'italic bold'),width=25,relief=RIDGE,borderwidth=9,activebackground='green',command=exit)
exit_button.pack(side=TOP,expand=True)

root.mainloop() # holds GUI window until closed


# activebackground='color': when press button,backgroundcolor changes
# activeforeground='color': when press button,textcolor changes