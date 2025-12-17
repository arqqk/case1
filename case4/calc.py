import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == 'sum':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            result = num1 / num2
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа")
    except ZeroDivisionError as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Калькулятор")

# Ввод числа 1
entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=0, padx=5, pady=5)

# Ввод числа 2
entry2 = tk.Entry(root, width=15)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Кнопки операций
btn_sum = tk.Button(root, text="Сумма", width=10, command=lambda: calculate('sum'))
btn_sum.grid(row=1, column=0, padx=5, pady=5)

btn_subtract = tk.Button(root, text="Разность", width=10, command=lambda: calculate('subtract'))
btn_subtract.grid(row=1, column=1, padx=5, pady=5)

btn_multiply = tk.Button(root, text="Произведение", width=10, command=lambda: calculate('multiply'))
btn_multiply.grid(row=2, column=0, padx=5, pady=5)

btn_divide = tk.Button(root, text="Деление", width=10, command=lambda: calculate('divide'))
btn_divide.grid(row=2, column=1, padx=5, pady=5)

# Окно вывода результата
label_result = tk.Label(root, text="Результат:", font=("Arial", 14))
label_result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
