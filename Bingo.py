import tkinter as tk
import random
from tkinter import messagebox

called_num = []

# Draw number
def draw_number():

    next_number = random.choice([i for i in range(1, 76) if i not in called_num])
    called_num.append(next_number)

    num_label.config(text=f"Number: {next_number}")
    his_label.config(text="履歴: " + ", ".join(map(str, called_num)))

#Reset game
def reset_game():
    global called_num
    called_num = []
    num_label.config(text="Next　を押してください")
    his_label.config(text="履歴: ")

# main window
root = tk.Tk()
root.title(u"ビンゴ大会")
root.geometry("400x300")

num_label = tk.Label(root, text=u'Number :', font=("Times", 24))
num_label.pack(pady=25)

his_label = tk.Label(root, text=u'履歴 :', font=("Times", 14))
his_label.pack(pady=25)

next_button = tk.Button(root, text=u'Next', font=("Times",14), width=15, command=draw_number)
next_button.pack(pady=15)

reset_button = tk.Button(root, text=u'Reset', font=("Times",14), width=15, command=reset_game)
reset_button.pack(pady=15)

root.mainloop()
