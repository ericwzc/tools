__author__ = 'erwang'

from tkinter import *
from boolcut import simplify

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Buttons")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH,expand=1)

        self.expLabel = Label(frame, anchor=N, justify=LEFT, text="Your Boolean Expression:", height=1)
        self.expLabel.pack(side=TOP)
        self.txtbox = Text(frame, height=5)
        self.txtbox.pack(side=TOP)
        self.outputLabel = Label(frame, anchor=W, justify=LEFT, wraplength=283, fg='blue')
        self.outputLabel.pack(side=TOP)

        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Clear", command=self.clear)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="Optimize", command=self.optimize)
        okButton.pack(side=RIGHT)

    def clear(self):
        self.txtbox.replace(1.0, END, "")
        self.outputLabel['text'] = ""

    def optimize(self):
        self.outputLabel['text'] = simplify(self.txtbox.get(1.0, END))


def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
