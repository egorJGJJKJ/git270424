from tkinter import *

root = Tk() #Создаём главное окно
root.attributes('-fullscreen',True)#Окно на весь экран

lbl = Label(root, text="Введи ключ и нажми ctrl+c", font= ('Comic Sans MS', 36), fg="purple")#Создание текста
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)#Размещение текста по центру relx и rely
#задают смещение элемента по горизонтали и вертикали относительно родителя (принимают значения от 0.0 до 1.0)
ent = Entry(root, fg='black', bg = 'orange', width = 50)
ent.place(relx = 0.5, rely = 0.6, anchor = CENTER)
root.mainloop()
