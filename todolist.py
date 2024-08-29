from tkinter import * 

def add_task():
    t = t_entry.get()
    d = enter_date.get()
    if t and d :
        lw.insert(END , f"{t} - {d}")
        t_entry.delete(0 , END)
        enter_date.delete(0 , END)

def delete_task():
    selected_task = lw.curselection()
    if selected_task :
        lw.delete(selected_task)


application_window = Tk()
application_window.title("To Do List")
application_window.geometry("550x700")
application_window.config(bg = "grey")
application_window.resizable(False , False)  

heading= Label(application_window , text="To-Do List", font= ("Helvetica", 12, "bold"), bg="lightblue")
heading.pack(pady=10)


#Enter the task
l_entry  = Label(application_window , text ="Enter task:" ,font= ("Helvetica", 12, "bold"), bg="lightblue" )
l_entry.pack(pady = 10)
t_entry = Entry(application_window , width = 50)
t_entry.pack(pady = 10)
#enter the date
l_date  = Label(application_window , text ="Enter Date to Complete:" ,font= ("Helvetica", 12, "bold"), bg="lightblue" )
l_date.pack(pady = 10)
enter_date = Entry(application_window , width = 50)
enter_date.pack(pady = 10)
#Confirm button
b_entry = Button(application_window , text = "ADD TASK " ,width = 15, font =('Helvetica' , 10, "bold") ,bd = 2 , bg = 'green' , command = add_task)
b_entry.pack(pady = 10)

lw = Listbox(
    application_window , 
    width = 25,
    height = 10,
    font = ('Helvetica' , 14),
    bd = 2,
    fg = 'black',
    activestyle= "none",
    selectbackground= 'grey'
)
lw.pack(pady = 10)

b_delete = Button(application_window , text = "DELETE TASK" , width = 15 , font = ('Helvetica ' , 12, "bold") , bd = 2 , bg = 'red' , command = delete_task )
b_delete .pack(pady=10)

       
application_window.mainloop()

