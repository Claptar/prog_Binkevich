import tkinter as tk

root = tk.Tk()
root.geometry('800x600')


def my_button_handler(event):
    var.set(1)

var = tk.IntVar(root, 1)
label = tk.Label(root, text="Do you want to marry me ?", font="Arial 30")
rbutton1 = tk.Radiobutton (root, text= "Да", variable=var, value=1,font="Arial 30")
rbutton2 = tk.Radiobutton (root, text= "Нет", variable=var, value=2, font="Arial 30")
button1 = tk.Button(root, text="OK", font="Arial 30")
button1.pack()

for widget in label, rbutton1, rbutton2, button1:
    widget.pack()

button1.bind("<Motion>", my_button_handler)

root.mainloop()
