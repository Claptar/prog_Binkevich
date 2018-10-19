from tkinter import *

root = Tk()
root.geometry('800x600')        # размер окна 800x600
entry =Entry (width=20)
button = Button(text="Do thing")
label= Label (bg="black",fg="white",width=20)
def srt_to_sort_str (event):
    s=entry.get()
    s=s.split()
    s.sort()
    label['text'] = ''.join(s)
button.bind('<Button-1>',srt_to_sort_str)
entry.pack(side=BOTTOM)
button.pack(side=BOTTOM)
label.pack(side=BOTTOM)
mainloop()

from tkinter import *

root = Tk()
root.geometry('800x600')        # размер окна 800x600
canv = Canvas(root, bg='white') # создать в окне root, фон - белый
canv.pack(fill=BOTH, expand=1)  # размер - максимально возможный в обе стороны

# рисуем простые фигуры
canv.create_rectangle(50, 50, 100, 100, fill='red')
canv.create_line(0, 0, 150, 300, width=5)
canv.create_oval(200, 200, 500, 500)
canv.create_text(350, 350, text=u'МФТИ')

mainloop()