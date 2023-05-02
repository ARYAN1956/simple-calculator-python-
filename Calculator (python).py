import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title('Calculator')

       
        self.display = tk.Entry(master, width=25, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

       
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]
        self.buttons = []
        for i, text in enumerate(button_texts):
            row, col = divmod(i, 4)
            button = tk.Button(master, text=text, width=5, height=2)
            button.grid(row=row+1, column=col, padx=2, pady=2)
            self.buttons.append(button)

       
        for i, button in enumerate(self.buttons):
            if button_texts[i].isdigit():
                button.config(command=lambda x=button_texts[i]: self.add_to_display(x))
            elif button_texts[i] == '.':
                button.config(command=lambda: self.add_to_display('.'))
            elif button_texts[i] == 'C':
                button.config(command=self.clear_display)
            elif button_texts[i] == '+':
                button.config(command=lambda: self.add_to_display('+'))
            elif button_texts[i] == '-':
                button.config(command=lambda: self.add_to_display('-'))
            elif button_texts[i] == '*':
                button.config(command=lambda: self.add_to_display('*'))
            elif button_texts[i] == '/':
                button.config(command=lambda: self.add_to_display('/'))

        # Add equals button
        equals_button = tk.Button(master, text='=', width=5, height=2)
        equals_button.grid(row=5, column=3, padx=2, pady=2)
        equals_button.config(command=self.evaluate_expression)

    def add_to_display(self, value):
        self.display.insert('end', value)

    def clear_display(self):
        self.display.delete(0, 'end')

    def evaluate_expression(self):
        try:
            result = eval(self.display.get())
            self.clear_display()
            self.add_to_display(str(result))
        except:
            self.clear_display()
            self.add_to_display('Error')

root = tk.Tk()
app = Calculator(root)
root.mainloop()
