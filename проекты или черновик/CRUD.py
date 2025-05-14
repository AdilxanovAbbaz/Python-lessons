from tkinter import *

class Kalkulator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x320")
        self.root.title("Калькулятор")
        self.expr = ""
        self.draw()

    def draw(self):
        self.entry = Entry(self.root, font=("Arial", 20), justify=RIGHT)
        self.entry.place(x=20, y=20, width=260, height=40)

        btns = [
            ('7',20,80),('8',80,80),('9',140,80),('/',200,80),
            ('4',20,130),('5',80,130),('6',140,130),('*',200,130),
            ('1',20,180),('2',80,180),('3',140,180),('-',200,180),
            ('0',20,230),('C',80,230),('=',140,230),('+',200,230)
        ]

        for txt,x,y in btns:
            Button(self.root, text=txt, font=("Arial",14), width=4, height=2,
                   command=lambda t=txt: self.click(t)).place(x=x, y=y)

        self.root.mainloop()

    def click(self, ch):
        if ch == "=":
            self.entry.delete(0, END)
            self.entry.insert(END, self.Kalkulator(self.expr))
            self.expr = self.entry.get()
        elif ch == "C":
            self.expr = ""
            self.entry.delete(0, END)
        else:
            self.expr += ch
            self.entry.delete(0, END)
            self.entry.insert(END, self.expr)

    def Kalkulator(self, e):
        for o in "+-*/":
            if o in e:
                a, b = e.split(o)
                if a.isdigit() and b.isdigit():
                    a, b = int(a), int(b)
                    return str(a+b) if o=="+" else str(a-b) if o=="-" else str(a*b) if o=="*" else str(a//b) if b!=0 else "Ошибка"
        return "Ошибка"

if __name__ == "__main__":
    Kalkulator()
