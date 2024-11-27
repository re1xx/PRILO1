import os
from random import randint
from tkinter import Tk, Button, Label, Entry, messagebox, StringVar, Frame
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
import math
import random

# Функция для генерации случайных чисел и записи их в файл
def generate():
    # Открываем диалоговое окно для выбора файла
    file_name = askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", "*.*")])
    if not file_name:  # Проверяем, выбран ли файл
        messagebox.showinfo("Info", "Файл не выбран")
        return
    # Записываем 10 случайных чисел в файл
    with open(file_name, 'w') as temp_file:
        for _ in range(10):
            temp_file.write(str(randint(1, 100)) + " ")            
    # Читаем содержимое файла и выводим его
    with open(file_name, 'r') as temp_file:
        content = temp_file.read()
        output.set("Содержимое: " + content)
        number = list(map(int, content.split()))
        if number:  # Если числа найдены, вычисляем среднее
            average = sum(number) / len(number)
            output.set(output.get() + f"\nСр. значение: {average:.2f}")
        else:
            output.set(output.get() + "\nФайл пуст")

# Функция для вывода приветствия
def hello():
    result = "Привет!"
    output.set(result)

# Функция для генерации случайных чисел, нахождения максимального и минимального значений
def rannum():
    a = [random.randint(1, 99) for i in range(10)]
    a.sort()  # Сортируем список
    max_num = max(a)  # Находим максимальное число
    min_num = min(a)  # Находим минимальное число
    result = f'max = {max_num}; min = {min_num}; sum = {sum(a)}'
    output.set(result)

# Функция для выполнения базовых математических операций
def math_operations():
    try:
        a = int(entry_a.get())  # Получаем первое число
        b = int(entry_b.get())  # Получаем второе число
        results = [
            f'{a} + {b} = {a + b}', 
            f'{a} - {b} = {a - b}',
            f'{a} * {b} = {a * b}'
        ]
        if b != 0:  # Проверяем, не делим ли на ноль
            results.append(f'{a} / {b} = {a / b:.2f}')
        else:
            results.append("Деление на 0 невозможно")
        
        output.set("\n".join(results))  # Выводим результаты операций
    except ValueError:  # Обрабатываем ошибки, если введены не числа
        output.set("Пожалуйста, введите действительные числа.")

# Основное окно приложения
root = Tk()
root.title("Приложение")
root.geometry("800x450")
font1 = font.Font(family="Cambria", size=11, weight="bold", slant="roman")
output = StringVar()

# Основной фрейм
main_frame = Frame(root, bg='#900C3F')
main_frame.pack(pady=10)

# Фрейм для кнопок
button_frame = Frame(main_frame, bg='#900C3F')
button_frame.grid(row=0, column=0, padx=10, pady=10)

# Стиль кнопок
button_style = {
    'width': 30,
    'height': 2,
    'bg': '#C70039',
    'font': font1,
    'bord': 7,
    'foreground': '#581845',
}

# Кнопки вызова функций
Button(button_frame, text="Генерировать числа", command=generate, **button_style).grid(row=0, column=0, padx=0, pady=1)
Button(button_frame, text="Приветствовать", command=hello, **button_style).grid(row=2, column=0, padx=0, pady=1)
Button(button_frame, text="Случайные числа", command=rannum, **button_style).grid(row=3, column=0, padx=0, pady=1)

# Фрейм для остальных элементов
other_frame = Frame(main_frame, bg='#900C3F')
other_frame.grid(row=0, column=1, padx=10)

# Ввод данных
Label(other_frame, text="Первое число:", foreground='white', bg='#900C3F').pack()
entry_a = Entry(other_frame, width=20, bg='#F37A7A')
entry_a.pack(pady=5)
Label(other_frame, text="Второе число:", foreground='white', bg='#900C3F').pack()
entry_b = Entry(other_frame, width=20, bg='#F37A7A')
entry_b.pack(pady=5)

# Кнопка для выполнения математических операций
Button(other_frame, text="Выполнить математические операции", command=math_operations, font=font2, foreground='#581845', width=30, height=2, bg='#C70039', bord=7).pack(pady=20)

# Вывод результатов
other_frame1 = Frame(main_frame)
other_frame1.grid(row=0, column=1, padx=10)
output_label = Label(textvariable=output, wraplength=400, bg='#900C3F', foreground='white', width=70, height=20)
output_label.pack(pady=20)

# Запуск главного цикла приложения
root.mainloop()
