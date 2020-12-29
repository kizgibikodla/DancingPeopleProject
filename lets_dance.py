import random
import re
import tkinter as tk
from PIL import Image, ImageTk

master = tk.Tk()

master.geometry("1200x700")
master.resizable(width=False, height=False)
master.title("Dancing People!")

textBox = tk.Text(master, height=5, font =("Helvetica", 32))
textBox.configure(background="red")
textBox.place(x=300, y=300)
textBox.pack()

lbl1 = tk.Label(master, text="LET'S DANCE WITH YOUR LETTERS!!!", fg="red", font=("Arial", 50))
lbl1.place(x=100, y=300)

colors = ["red", "green", "blue", "yellow", "orange", "brown", "cyan", "purple"]


def label_UI():
    randomized = []
    for i in range(3):
        randomized.append(random.choice(colors))
    lbl1 = tk.Label(master, text="LET'S DANCE WITH YOUR LETTERS!!!", fg=randomized[1], font=("Arial", 50))
    lbl1.place(x=100, y=300)


def update_label():
    label_UI()
    master.after(500, update_label)

def letter_to_int(letter):
    alphabet = list('abcçdefgğhıijklmnoöpqrsştuüvwxyz1234567890')
    return alphabet.index(letter)+1


def get_text_input():
    result = textBox.get("1.0","end")
    result.lower().rstrip()
    result = re.sub(r'\W+', '', result)
    slide_val=0
    if len(result) != 0:
        update_label()
        for i, ch in enumerate(result):
            find_figure_num = letter_to_int(ch)
            load = Image.open("image/" + str(find_figure_num)+".png")
            render = ImageTk.PhotoImage(load)
            img = tk.Label(master, image=render)
            img.image = render
            slide_val = slide_val + 80
            img.place(x=100+slide_val, y=400)
    else:
        print("Dans edeceğin bir kelime gir!")


def clearBox():
    textBox.delete("1.0", "end")
    load = Image.open("image/blank.png")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(master, image=render)
    img.image = render
    img.place(x=150, y=400)


btn_play = tk.Button(master, height=1, width=10, text="PLAY", command=get_text_input)
btn_play.pack(padx=(10, 10))

btn_change = tk.Button(master, height=1, width=10, text="CHANGE", command=clearBox)
btn_change.pack(padx=(10, 10))

btn_stop = tk.Button(master, height=1, width=10, text="STOP", command=master.quit)
btn_stop.pack(padx=(10, 10))


master.mainloop()