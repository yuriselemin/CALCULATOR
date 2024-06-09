

import tkinter as tk



def get_value():
    numb1 = int(number1_entry.get())
    numb2 = int(number2_entry.get())
    return numb1, numb2

def isert_value(value):
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, value)

def add():
    numb1, numb2 = get_value()
    res = numb1 + numb2
    isert_value(res)

    # numb1, numb2 = get_value()
def sub():
    numb1, numb2 = get_value()
    res = numb1 - numb2
    isert_value(res)

def mul():
    numb1, numb2 = get_value()
    res = numb1 * numb2
    isert_value(res)

def div():
    numb1, numb2 = get_value()
    res = numb1 / numb2
    isert_value(res)


window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x380")
window.resizable(False, False)

button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=67, y=200)
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=120, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=166, y=200)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=218, y=200)

number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=67, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=67, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=67, y=300)

number1 = tk.Label(window, text="Введите первое число: ")
number1.place(x=67, y=50)
number1 = tk.Label(window, text="Введите второе число: ")
number1.place(x=67, y=125)
number1 = tk.Label(window, text="Ответ: ")
number1.place(x=67, y=275)

window.mainloop()