from tkinter import *

class Esapshi:
    def __init__(self):
        self.root = Tk()
        win=self.root.geometry("300x400")
        self.root.title("Математик")
        self.expr = ""
        self.Sogiw()

    def Sogiw(self): #кнопки
        self.Kiritiw = Entry(self.root, font=("Arial", 20), justify=RIGHT)
        self.Kiritiw.place(x=20, y=20, width=260, height=40)

        b1 = Button(self.root, text="7", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("7"))
        b1.place(x=20, y=80)

        b2 = Button(self.root, text="8", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("8"))
        b2.place(x=80, y=80)

        b3 = Button(self.root, text="9", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("9"))
        b3.place(x=140, y=80)

        b4 = Button(self.root, text="/", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("/"))
        b4.place(x=200, y=80)

        b5 = Button(self.root, text="4", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("4"))
        b5.place(x=20, y=130)

        b6 = Button(self.root, text="5", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("5"))
        b6.place(x=80, y=130)

        b7 = Button(self.root, text="6", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("6"))
        b7.place(x=140, y=130)

        b8 = Button(self.root, text="*", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("*"))
        b8.place(x=200, y=130)

        b9 = Button(self.root, text="1", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("1"))
        b9.place(x=20, y=180)

        b10 = Button(self.root, text="2", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("2"))
        b10.place(x=80, y=180)

        b11 = Button(self.root, text="3", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("3"))
        b11.place(x=140, y=180)

        b12 = Button(self.root, text="-", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("-"))
        b12.place(x=200, y=180)

        b13 = Button(self.root, text="C", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("C"))
        b13.place(x=80, y=230)  

        b14 = Button(self.root, text="0", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("0"))
        b14.place(x=20, y=230)

        b15 = Button(self.root, text="=", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("="))
        b15.place(x=140, y=230)

        b16 = Button(self.root, text="+", font=("Arial", 14), width=4, height=2, command=lambda: self.Basilgan("+"))
        b16.place(x=200, y=230)

    def Basilgan(self, abb):
        if abb == "=":
            self.Kiritiw.delete(0, END)
            self.Kiritiw.insert(END, self.calc(self.expr))
            self.expr = self.Kiritiw.get()
        elif abb == "C":
            self.expr = ""
            self.Kiritiw.delete(0, END)
        else:
            self.expr += abb
            self.Kiritiw.delete(0, END)
            self.Kiritiw.insert(END, self.expr)

    def calc(self, e):
        for o in "+-*/":
            if o in e:
                a, b = e.split(o)
                if a.isdigit() and b.isdigit():
                    a, b = int(a), int(b)
                    return str(a + b) if o == "+" else str(a - b) if o == "-" else str(a * b) if o == "*" else str(a // b) if b != 0 else "Ошибка"
        return "Qate"
        
if __name__ == "__main__":
    Esapshi()