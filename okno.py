from tkinter import Tk, Label, Button

kliki = 0

def click_action(button):
    global kliki
    kliki +=1
    button.config(text=f'O działa! x {kliki}')

# def create_command(func,*args,**kwargs):
#     def command():
#         return func(*args,**kwargs)
#     return command

root = Tk()
root.title("Moja pierwsza aplikacja")
root.geometry("600x400")
label = Label(root, text="Spójrz na mnie!", font=25, fg="blue")
click_button = Button(root, text="Kliknij !", width=10)
click_button.config(command=lambda: click_action(click_button))

click_button.pack()
label.pack()

root.mainloop()
