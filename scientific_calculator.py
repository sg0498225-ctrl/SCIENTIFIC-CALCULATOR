import tkinter as tk
import math

# Just a small calculator class - written casually
class MySciCalc:
    def __init__(self, root):
        
        self.root = root
        root.title("Scientific Calculator")
        root.geometry("400x600")
        root.resizable(False, False)

        # storing what user types
        self._exp = ""
        self.show_var = tk.StringVar()  

        # --------- screen box ----------
        top_part = tk.Frame(root, highlightbackground="black", highlightthickness=2)
        top_part.pack(side="top", fill="x")

        self.screen = tk.Entry(
            top_part, 
            textvariable=self.show_var,
            font=("Arial",18),
            justify="right",
            bd=0,
            bg="#e9e9e9"
        )
        self.screen.pack(ipady=10, fill="x")

        # --------- main button area ----------
        area = tk.Frame(root, bg="grey")
        area.pack(fill="both")

        # NOTE: buttons placed manually (not using loops)
        self._make(area, "C", 0,0, cmd=self.clear_all, span=4, big=True)

        self._make(area,"7",1,0,lambda:self.put("7"))
        self._make(area,"8",1,1,lambda:self.put("8"))
        self._make(area,"9",1,2,lambda:self.put("9"))
        self._make(area,"/",1,3,lambda:self.put("/"))

        self._make(area,"4",2,0,lambda:self.put("4"))
        self._make(area,"5",2,1,lambda:self.put("5"))
        self._make(area,"6",2,2,lambda:self.put("6"))
        self._make(area,"*",2,3,lambda:self.put("*"))

        self._make(area,"1",3,0,lambda:self.put("1"))
        self._make(area,"2",3,1,lambda:self.put("2"))
        self._make(area,"3",3,2,lambda:self.put("3"))
        self._make(area,"-",3,3,lambda:self.put("-"))

        self._make(area,"0",4,0,lambda:self.put("0"), span=2)
        self._make(area,".",4,2,lambda:self.put("."))
        self._make(area,"+",4,3,lambda:self.put("+"))

        # scientific row
        self._make(area,"sin",5,0,lambda:self.do_sci("sin"))
        self._make(area,"cos",5,1,lambda:self.do_sci("cos"))
        self._make(area,"tan",5,2,lambda:self.do_sci("tan"))
        self._make(area,"log",5,3,lambda:self.do_sci("log"))

        self._make(area,"sqrt",6,0,lambda:self.do_sci("sqrt"))
        self._make(area,"exp",6,1,lambda:self.do_sci("exp"))
        self._make(area,"pi",6,2,lambda:self.put(str(math.pi)))
        self._make(area,"e",6,3,lambda:self.put(str(math.e)))

        self._make(area,"=",7,0,self.equals, span=4, big=True)

    # making button
    def _make(self, parent, txt, r, c, cmd=None, span=1, big=False):
        w = 33 if big else 10
        tk.Button(parent, text=txt, width=w, height=3, bd=0,
                  command=cmd, bg="white").grid(
                      row=r, column=c, columnspan=span, padx=1, pady=1
                  )

    # add items to expression
    def put(self, x):
        self._exp = self._exp + str(x)
        self.show_var.set(self._exp)

    def clear_all(self):
        self._exp = ""
        self.show_var.set("")

    # scientific operations
    def do_sci(self, what):
        try:
            val = float(self._exp)
            if what == "sin":
                res = math.sin(val)
            elif what == "cos":
                res = math.cos(val)
            elif what == "tan":
                res = math.tan(val)
            elif what == "log":
                res = math.log10(val)
            elif what == "sqrt":
                res = math.sqrt(val)
            else:
                res = math.exp(val)

            self._exp = str(res)
            self.show_var.set(res)

        except Exception:
            self.show_var.set("Error")
            self._exp = ""

    # normal calc
    def equals(self):
        try:
            ans = str(eval(self._exp))
            self.show_var.set(ans)
            self._exp = ans
        except:
            self.show_var.set("Error")
            self._exp = ""


if __name__ == "__main__":
    r = tk.Tk()
    MySciCalc(r)
    r.mainloop()
