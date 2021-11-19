from random import choice
from tkinter import Tk, Label, Button

available_choices = ['paper', 'rock', 'scissors']


def play(player, cpu):
    win_with = {'paper': 'rock',
                'rock': 'scissors',
                'scissors': 'paper'}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text="REMIS", fg='blue')
    elif is_user_winner:
        text_label.config(text="Wygrałeś!", fg='green')
    else:
        text_label.config(text="Wygrałem, HA HA!", fg='red')


root = Tk()
root.title("Gra - kamień, papier, nożyce")
root.geometry("400x300")
text_label = Label(root, font=50, text='Zagrajmy!')
text_label.pack()
Button(root, text="📝 Papier", font=50, command=lambda: play_cmd("paper")).pack()
Button(root, text="🛑 Kamień", font=50, command=lambda: play_cmd("rock")).pack()
Button(root, text="✂️ Nożyce", font=50, command=lambda: play_cmd("scissors")).pack()

root.mainloop()
