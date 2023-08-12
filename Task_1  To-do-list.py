from tkinter import * 

# Button funcitons 
def ADD():
    task= entry.get()
    if task :
        listbox.insert(END,task)
        entry.delete(0,END)
def Del():
    task = listbox.curselection()
    if task:
        listbox.delete(task)

#EDIT FUNCTION
def EDIT():
    select_task= listbox.curselection()
    task = entry.get()
    if select_task and task:
        edit_task =listbox.get(select_task)
        listbox.delete(select_task)
        listbox.insert(0,task)
    elif select_task:
        edit_task = listbox.get(select_task)
        entry.delete(0,'end')
        entry.insert(0,edit_task)

def clear():
    listbox.delete(0,'end')

win = Tk()
win.title("To-Do-List")
win.geometry("350x450+550+180")
win.resizable(width=False,height=False)
label_1 = Label(win,text="To Do List",font='ivay 18 bold',fg='red')
label_1.pack(fill=BOTH)

#frame for containg listbox
frame_1 =Frame(win,height=180,width=300)
frame_1.place(x=20,y=70)

#listbox 
listbox = Listbox(frame_1,highlightthickness=0,height=10,width=300,fg='black',bg="white",bd=5)
listbox.place(x=0,y=0)
#frame for entry bar

frame_2 = Frame(win,height=20,width=200,bg='red')
frame_2.place(x=20,y=280)
#entry bar 

entry=Entry(frame_2,width=20,font=('ivay 15'),bd=5)
entry.pack()

#add  button
add =Button(win,text='ADD',bg='orange',fg='black',font='ivay 10',command=ADD,bd=5,width=6)
add.place(x=260,y=277)
#delete button
delete_button =Button(win,text='DELETE',bg='orange',fg='black',font='ivay 10',command=Del,bd=5)
delete_button.place(x=20,y=330)

edit_button =Button(win,text='EDIT/UPDATE',bg='orange',fg='black',font='ivay 10',command=EDIT,bd=5,width=10)
edit_button.place(x=120,y=330)

#clear button 
clear_button =Button(win,text='CLEAR',bg='orange',fg='black',font='ivay 10',command=clear,bd=5,width=6)
clear_button.place(x=240,y=330)



win.mainloop()