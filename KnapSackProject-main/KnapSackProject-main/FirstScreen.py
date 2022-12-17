import tkinter as tk
from tkinter import messagebox
import FirstScreen_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Knapsackfirst (root)
    FirstScreen_support.init(root, top)
    root.mainloop()

w = None

class Knapsackfirst:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("400x300+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Knapsack_project")
        top.configure(background="#dcedc8")


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.1, rely=0.2, height=21, width=314)
        self.Label1.configure(background="#dcedc8")
        self.Label1.configure(font="-family {System} -size 10 -weight bold")
        self.Label1.configure(foreground="#212121")
        self.Label1.configure(text='''Select 0-1_knapsack or unbounded_knapsack''')
        
        c_v = tk.StringVar(root)
        self.x =0


        def checkB():
            if c_v.get() == 'Yes':
                self.UnboundKnapsack.config(state="disable")
                self.x =  1
            else:
                self.UnboundKnapsack.config(state="normal")
                self.x = 0
            return self.x

        def check01():
            if c_v.get() == 'No':
                self.knapsack01.config(state="disable")
                self.x =  1
            else:
                self.knapsack01.config(state="normal")
                self.x = 0
            return self.x


        self.knapsack01 = tk.Checkbutton(top)
        self.knapsack01.place(relx=0.1, rely=0.4, relheight=0.083 , relwidth=0.303)
        self.knapsack01.configure(background="#dcedc8")
        self.knapsack01.configure(font="-family {System} -size 10 -weight bold")
        self.knapsack01.configure(justify='left')
        self.knapsack01.configure(text='''0_1_Knapsack''')
        self.knapsack01.configure(variable=c_v) 
        self.knapsack01.configure(onvalue='Yes', offvalue='')
        self.knapsack01.configure(command=checkB)

        self.UnboundKnapsack = tk.Checkbutton(top)
        self.UnboundKnapsack.place(relx=0.4, rely=0.4, relheight=0.083 , relwidth=0.453)
        self.UnboundKnapsack.configure(background="#dcedc8")
        self.UnboundKnapsack.configure(font="-family {System} -size 10 -weight bold")
        self.UnboundKnapsack.configure(foreground="#000000")
        self.UnboundKnapsack.configure(text='''Unbounded_Knapsack''')
        self.UnboundKnapsack.configure(variable=c_v) 
        self.UnboundKnapsack.configure(onvalue='No', offvalue='')
        self.UnboundKnapsack.configure(command=check01)


        def ok():
            i=checkB()
            j=check01()
            if i == 1 or j==1:

               if i == 1:
                FirstScreen_support.destroy_window()
                import Knapsack
                Knapsack.vp_start_gui()

               elif j == 1:
                FirstScreen_support.destroy_window()
                import UnboundedKnapsack
                UnboundedKnapsack.vp_start_gui()

            else :
                messagebox.showerror("!!!!!!!", "PlEASE, make a selection :)")

        self.selectKbtn = tk.Button(top)
        self.selectKbtn.place(relx=0.4, rely=0.666, height=34, width=47)
        self.selectKbtn.configure(background="#dcedc8")
        self.selectKbtn.configure(borderwidth="3")
        self.selectKbtn.configure(font="-family {System} -size 10 -weight bold")
        self.selectKbtn.configure(text='''OK''')
        self.selectKbtn.configure(command=ok)





