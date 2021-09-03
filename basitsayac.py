from tkinter import *
from tkinter import messagebox

window = Tk()


sayi = 0
def calistir():
    global sayi
    sayi += 1
    label.config(text = sayi)



window.title("İlk Projem")
window.geometry("400x300")

label = Label(window, text="0", font="Arial 20")
label.pack()
btn = Button(window, text="Tıkla", command=calistir)
btn.pack()


window.mainloop()