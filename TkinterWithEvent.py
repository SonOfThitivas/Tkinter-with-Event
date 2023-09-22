from tkinter import *

class UI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Case")
        self.create_widgets()
        
    def create_widgets(self):
        self.entry = Entry(self, font=("Arial",25), width=10)
        self.entry.bind('<BackSpace>', self.user_return)
        self.entry.bind('<Key>', self.user_key)
        self.entry.pack()
        
        self.resultPlus = 0
        self.resultMinus = 0
        
        Label(self, text="Plus when user presses any keys.", font=("Arial",25)).pack()
        self.l1 = Label(self, text=self.resultPlus, font=("Arial",25))
        self.l1.pack()
        Label(self, text="Minus when user presses backspace.", font=("Arial",25)).pack()
        self.l2 = Label(self, text=self.resultMinus, font=("Arial",25))
        self.l2.pack()

    def user_key(self, event):
        self.resultPlus += 1
        self.l1.config(text=self.resultPlus)
        
    def user_return(self, event):
        self.resultMinus -= 1
        self.l2.config(text=self.resultMinus)
        
if __name__ == '__main__':
    wn = UI()
    wn.mainloop()