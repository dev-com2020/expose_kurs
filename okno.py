from tkinter import Tk, Label, Button, messagebox, Checkbutton, Radiobutton, Entry, Frame

kliki = 0
przelacznik = 0

def click_action(button):
    global kliki
    kliki += 1
    button.config(text=f'O działa! x {kliki}')


def klik():
    global root
    odp = messagebox.askquestion("Pytanie...", "Czy na pewno?")
    if odp == 'yes':
        root.destroy()


# def create_command(func,*args,**kwargs):
#     def command():
#         return func(*args,**kwargs)
#     return command

root = Tk()
root.title("Moja pierwsza aplikacja")
root.geometry("600x400")
ramka = Frame(root,height=400,width=600, bg="alice blue")
ramka.place(x=0,y=0)
label = Label(root, text="Spójrz na mnie!", font=60, fg="blue")
click_button = Button(root, text="Kliknij !", font=50, width=20, background='yellow')
click_button.config(command=lambda: click_action(click_button))
click_button.place(x=200, y=150)
button2 = Button(root, text="A co tutaj?", font=50, width=10, background='red')
button2.place(x=250, y=50)
button2.config(command=klik)
label2 = Label(root, text="Przycisk !", font=60, fg="blue")
label3 = Label(root, text="Przycisk!", font=60, fg="blue")
label4 = Label(root, text="Przycisk!", font=60, fg="blue")
label2.grid(row=0, column=0)
label3.grid(row=1, column=1)
label4.grid(row=2, column=0, columnspan=2)
czek = Checkbutton(root,text='Przełącznik',variable=przelacznik)
czek.grid(row=3,column=1)
radio = Radiobutton(root,text='Kawa',variable=przelacznik,value="kawa")
radio2 = Radiobutton(root,text='Herbata',variable=przelacznik,value="herbata")
radio.grid(row=4,column=1)
radio2.grid(row=4,column=2)
wejscie = Entry(root,width=30)
wejscie.place(x=350, y=20)

# click_button.pack()
#label.pack(side="bottom", fill="both")

root.mainloop()
