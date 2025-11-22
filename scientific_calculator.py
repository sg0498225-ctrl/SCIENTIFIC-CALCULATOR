import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#fff", cursor="hand2", command=self.clear).grid(row=0, column=0, columnspan=4, padx=1, pady=1)

        seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
        eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
        nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
        divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("/")).grid(row=1, column=3, padx=1, pady=1)

        four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
        five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
        six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
        multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("*")).grid(row=2, column=3, padx=1, pady=1)

        one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
        two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
        three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
        minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("-")).grid(row=3, column=3, padx=1, pady=1)

        zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
        plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("+")).grid(row=4, column=3, padx=1, pady=1)

        sin = tk.Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.scientific_click("sin")).grid(row=5, column=0, padx=1, pady=1)
        cos = tk.Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.scientific_click("cos")).grid(row=5, column=1, padx=1, pady=1)
        tan = tk.Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.scientific_click("tan")).grid(row=5, column=2, padx=1, pady=1)
        log = tk.Button(btns_frame, text="log", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.scientific_click("log")).grid(row=5, column=3, padx=1, pady=1)

        sqrt = tk.Button(btns_frame, text="sqrt", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.scientific_click("sqrt")).grid(row=6, column=0, padx=1, pady=1)
        exp = tk.Button(btns_frame, text="exp", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.scientific_click("exp")).grid(row=6, column=1, padx=1, pady=1)
        pi = tk.Button(btns_frame, text="pi", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(math.pi)).grid(row=6, column=2, padx=1, pady=1)
        e = tk.Button(btns_frame, text="e", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(math.e)).grid(row=6, column=3, padx=1, pady=1)

        equals = tk.Button(btns_frame, text="=", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self.equalpress).grid(row=7, column=0, columnspan=4, padx=1, pady=1)

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def scientific_click(self, func):
        try:
            if func == "sin":
                result = math.sin(float(self.expression))
            elif func == "cos":
                result = math.cos(float(self.expression))
            elif func == "tan":
                result = math.tan(float(self.expression))
            elif func == "log":
                result = math.log10(float(self.expression))
            elif func == "sqrt":
                result = math.sqrt(float(self.expression))
            elif func == "exp":
                result = math.exp(float(self.expression))
            self.input_text.set(result)
            self.expression = str(result)
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.input_text.set(total)
            self.expression = total
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    ScientificCalculator(root)
    root.mainloop()
