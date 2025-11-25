import tkinter as tk
from tkinter import messagebox
import math
import ast
import operator

"""
Professional, human-written Scientific Calculator
- Safely evaluates arithmetic expressions (limited subset)
- Applies scientific functions to the current displayed value
- Degree / Radian toggle to avoid confusion with trig functions
- Backspace, Clear, History (last results)
"""

# Allowed binary operators for safe eval
_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Mod: operator.mod,
}


def safe_eval(expr: str) -> float:
    """
    Evaluate a numeric expression safely using ast (supports + - * / ** % and unary +/-).
    Raises ValueError for unsupported expressions.
    """
    try:
        node = ast.parse(expr, mode="eval").body
        return _eval_node(node)
    except Exception as e:
        raise ValueError("Invalid expression") from e


def _eval_node(node):
    if isinstance(node, ast.Num):  # Python <3.8
        return node.n
    # For Python 3.8+, ast.Constant is used instead of ast.Num
    if hasattr(ast, "Constant") and isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed")
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError("Operator not allowed")
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _ALLOWED_OPERATORS[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError("Unary operator not allowed")
        operand = _eval_node(node.operand)
        return _ALLOWED_OPERATORS[op_type](operand)
    # disallow names, calls, etc.
    raise ValueError("Unsupported expression")


class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("420x620")
        master.resizable(False, False)

        # state
        self.expression = ""        # expression typed for normal eval
        self.display_var = tk.StringVar(value="")
        self.history = []          # store previous results
        self.use_degrees = True    # default: degrees (changeable by user)

        # layout
        self._build_display()
        self._build_buttons()

    # -------------------------
    # UI construction
    # -------------------------
    def _build_display(self):
        top = tk.Frame(self.master, highlightthickness=2, highlightbackground="#333")
        top.pack(side="top", fill="x", pady=(8, 0), padx=8)

        entry = tk.Entry(top, textvariable=self.display_var,
                         font=("Segoe UI", 18, "bold"),
                         justify="right", bd=0, bg="#f7f7f7")
        entry.pack(fill="x", ipady=12)

        # small informative label
        self.mode_label = tk.Label(self.master, text="Mode: Degrees", anchor="e")
        self.mode_label.pack(fill="x", padx=8)

    def _build_buttons(self):
        panel = tk.Frame(self.master, bg="#e6e6e6")
        panel.pack(fill="both", expand=True, padx=8, pady=10)

        # Row 0: Clear, Backspace, Mode toggle, History
        tk.Button(panel, text="C", width=8, height=2, command=self.clear).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(panel, text="⌫", width=8, height=2, command=self.backspace).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(panel, text="Deg/Rad", width=8, height=2, command=self.toggle_mode).grid(row=0, column=2, padx=4, pady=4)
        tk.Button(panel, text="History", width=8, height=2, command=self.show_history).grid(row=0, column=3, padx=4, pady=4)

        # Numeric and operator buttons
        keys = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3)
        ]
        for txt, r, c in keys:
            width = 8 if txt != "0" else 17
            if txt == "0":
                tk.Button(panel, text=txt, width=17, height=2, command=lambda t=txt: self._append(t)).grid(row=r, column=c, columnspan=2, padx=4, pady=4)
            else:
                tk.Button(panel, text=txt, width=8, height=2, command=lambda t=txt: self._append(t)).grid(row=r, column=c, padx=4, pady=4)

        # Scientific row
        sci = [
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3),
            ("sqrt", 6, 0), ("exp", 6, 1), ("pi", 6, 2), ("e", 6, 3)
        ]
        for txt, r, c in sci:
            tk.Button(panel, text=txt, width=8, height=2, command=lambda t=txt: self._scientific_action(t)).grid(row=r, column=c, padx=4, pady=4)

        # Equal button (bottom)
        tk.Button(panel, text="=", width=36, height=2, bg="#d6d6d6", command=self.evaluate).grid(row=7, column=0, columnspan=4, padx=4, pady=(8, 4))

    # -------------------------
    # Control actions
    # -------------------------
    def _append(self, ch: str):
        """Append character to the expression / display."""
        self.expression += str(ch)
        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def toggle_mode(self):
        self.use_degrees = not self.use_degrees
        mode_text = "Degrees" if self.use_degrees else "Radians"
        self.mode_label.config(text=f"Mode: {mode_text}")

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No previous results.")
            return
        # show recent 10 results
        lines = "\n".join(self.history[-10:][::-1])
        messagebox.showinfo("History (last results)", lines)

    # -------------------------
    # Evaluation & scientific functions
    # -------------------------
    def evaluate(self):
        if not self.expression.strip():
            return
        try:
            # Use safe_eval to avoid executing arbitrary code
            value = safe_eval(self.expression)
            # format and display
            out = self._format_number(value)
            self.display_var.set(out)
            self.expression = out  # allow chaining
            self.history.append(out)
        except ValueError:
            self.display_var.set("Error")
            self.expression = ""

    def _format_number(self, val: float) -> str:
        # show integer format when possible, else show float with trimming
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        # limit to 12 significant digits to avoid long floats
        return str(round(val, 12)).rstrip("0").rstrip(".") if "." in str(val) else str(val)

    def _scientific_action(self, func_label: str):
        """
        Applies scientific function to the current displayed number.
        Behavior:
        - If display is empty, do nothing.
        - We first evaluate current expression (safe_eval), then apply the selected function.
        - Handles degree<->radian conversion when needed.
        """
        text = self.display_var.get().strip()
        if not text:
            return

        try:
            # evaluate whatever is in display (it may be "3+4" etc.)
            base_val = safe_eval(text)
        except ValueError:
            self.display_var.set("Error")
            self.expression = ""
            return

        try:
            # mapping from label -> function that accepts a float and returns float
            if func_label == "sin":
                arg = math.radians(base_val) if self.use_degrees else base_val
                res = math.sin(arg)
            elif func_label == "cos":
                arg = math.radians(base_val) if self.use_degrees else base_val
                res = math.cos(arg)
            elif func_label == "tan":
                arg = math.radians(base_val) if self.use_degrees else base_val
                res = math.tan(arg)
            elif func_label == "log":
                if base_val <= 0:
                    raise ValueError("log domain error")
                res = math.log10(base_val)
            elif func_label == "sqrt":
                if base_val < 0:
                    raise ValueError("sqrt domain error")
                res = math.sqrt(base_val)
            elif func_label == "exp":
                res = math.exp(base_val)
            elif func_label == "pi":
                res = math.pi
            elif func_label == "e":
                res = math.e
            else:
                raise ValueError("Unknown function")

            out = self._format_number(res)
            self.display_var.set(out)
            self.expression = out
            self.history.append(out)
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()