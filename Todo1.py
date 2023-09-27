from tkinter import *
from tkinter import ttk

class todo:
    def _init_(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = label(self.root, text='To-Do-List-App',
                          font='ariel, 25 bold', width=10,bd=5, bg='blue', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = label(self.root, text='Add Text',
                            font='ariel, 18 bold', width=10,bd=5, bg='orange', fg='black')
        self.label2.place(x=40,y=54)
        self.label3 = label(self.root, text='Tasks',
                            font='ariel, 18 bold', width=10,bd=5, bg='orange', fg='black')
        self.label3.place(x=320,y=54)

    def main():
        root = Tk()
        vi = todo(root)
        root.mainloop()

if __name__ =="_main_":
    main()