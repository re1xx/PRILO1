import os
from random import randint
from tkinter import Tk, Button, Label, Entry, messagebox, StringVar, Frame
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
import math
import random

def generate():
    file_name = askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", "*.*")])
    if not file_name:
        messagebox.showinfo("Info", "Файл не выбран")
        return

    with open(file_name, 'w') as temp_file:
        for _ in range(10):
            temp_file.write(str(randint(1, 100)) + " ")
            
    with open(file_name, 'r') as temp_file:
        content = temp_file.read()
        output.set("Содержимое: " + content)
        number = list(map(int, content.split()))
        if number:
            average = sum(number) / len(number)
            output.set(output.get() + f"\nСр. значение: {average:.2f}")
        else:
            output.set(output.get() + "\nФайл пуст")

def hello():
    result = "Привет!"
    output.set(result)

def rannum():
    a = [random.randint(1, 99) for i in range(10)]
    a.sort()
    max_num = max(a)
    min_num = min(a)
    result = f'max = {max_num}; min = {min_num}; sum = {sum(a)}'
    output.set(result)

def math_operations():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        
        results = [f'{a} + {b} = {a + b}',
                   f'{a} - {b} = {a - b}',
                   f'{a} * {b} = {a * b}']
        
        if b != 0:
            results.append(f'{a} / {b} = {a / b:.2f}')
        else:
            results.append("Деление на 0 невозможно")
        
        output.set("\n".join(results))
    except ValueError:
        output.set("Пожалуйста, введите действительные числа.")

root = Tk()
root.title("Приложение")
root.geometry("800x450")
font1 = font.Font(family="Cambria", size=11, weight="bold", slant="roman")
output = StringVar()
C = Canvas(bg="blue", height=500, width=300)
#photo = PhotoImage(file = "..//Снимок экрана 2023-08-13 224050.png")
#label = Label(root, image=photo)
#label.place(x=0, y=0, relwidth=1, relheight=1)
font2 = font.Font(family="Cambria", size=7, weight="normal", slant="roman")
output = StringVar()
# Основной фрейм
main_frame = Frame(root, bg='#900C3F')
main_frame.pack(pady=10)

# Фрейм для кнопок
button_frame = Frame(main_frame, bg='#900C3F')
button_frame.grid(row=0, column=0, padx=10, pady=10)

button_style = {
'width': 30,
'height': 2,
'bg': '#C70039',
'font': font1,
'bord': 7,
'foreground':'#581845',
}

Button(button_frame, text="Генерировать числа", command=generate, **button_style).grid(row=0, column=0, padx=0, pady=1 )
Button(button_frame, text="Приветствовать", command=hello, **button_style).grid(row=2, column=0, padx=0, pady=1)
Button(button_frame, text="Случайные числа", command=rannum, **button_style).grid(row=3, column=0, padx=0, pady=1)

# Фрейм для остальных элементов
other_frame = Frame(main_frame, bg='#900C3F')
other_frame.grid(row=0, column=1, padx=10)

Label(other_frame, text="Первое число:", foreground='white', bg='#900C3F').pack()
entry_a = Entry(other_frame, width=20, bg='#F37A7A')
entry_a.pack(pady=5)

Label(other_frame, text="Второе число:", foreground='white', bg='#900C3F').pack()
entry_b = Entry(other_frame, width=20, bg='#F37A7A')
entry_b.pack(pady=5)

Button(other_frame, text="Выполнить математические операции", command=math_operations, font=font2, foreground='#581845', width=30, height=2, bg= '#C70039', bord=7).pack(pady=20)
other_frame1 = Frame(main_frame)
other_frame1.grid(row=0, column=1, padx=10)
output_label = Label(textvariable=output, wraplength=400, bg='#900C3F', foreground='white', width=70, height=20)
output_label.pack(pady=20)

root.mainloop()