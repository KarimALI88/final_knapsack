import os
import sys
import tkinter as tk
from tkinter.constants import COMMAND
from tkinter import messagebox
import UnboundedKnapsack_DA
import FirstScreen_support
import UnboundedKnapsack_GA


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = UNBOUNDEDKNAPSACK (root)
    FirstScreen_support.init(root, top)
    root.mainloop()


items =[( 5 , 21 ),( 4 , 45 ),( 15 , 53 ),( 3 , 41 ) , ( 7 , 17 ) , ( 18 , 60 )] #[(weight , value)]
w = None

class UNBOUNDEDKNAPSACK:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#e1f5fe'
        _fgcolor = '#000000'
        _compcolor = '#e1f5fe'
        _ana1color = '#e1f5fe'
        _ana2color = '#e1f5fe'

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Unbounded Knapsack")
        top.configure(background="#dcedc8")

        self.weigth = tk.Label(top)         
        self.weigth.place(relx=0.0, rely=0.044, height=31, width=200)
        self.weigth.configure(background="#dcedc8")
        self.weigth.configure(font="-family {System} -size 10 -weight bold")
        self.weigth.configure(text='''Knapsack_Weigth''')

        self.weigthNum = tk.Entry(top)
        self.weigthNum.place(relx=0.3, rely=0.044, height=30, relwidth=0.073)
        self.weigthNum.configure(background="white")
        self.weigthNum.configure(borderwidth="2")
        self.weigthNum.configure(font="TkFixedFont")

        # function to control the entered weigth (bigger than 125)
        def weigthCheck():
              weigthNum = self.weigthNum.get()
              if int(weigthNum) < 125:
                     return True
              else:
                     return False


        def SelectedAlgorithm():
            weigthNum = self.weigthNum.get()
            i=check()
            j=c()
            if i == 1 or j == 1:
              if i == 1:
                     ChoosedIndiv = UnboundedKnapsack_GA.UnboundedKnap_GA().run(items , int(weigthNum) , 20)
                     return ChoosedIndiv 
              elif j == 1:
                     ChoosedIndiv = UnboundedKnapsack_DA.UnboundedKnap_DA().run(items , int(weigthNum) , 20)
                     return ChoosedIndiv 

            else: 
                messagebox.showerror("Warning", "PlEASE, make a selection :)")


        c_v = tk.StringVar(root)
        self.x = 0
        def check():
            if c_v.get() == 'Yes':
                self.DE.config(state="disable")
                self.x =  1
            else:
                self.DE.config(state="normal")
                self.x = 0
            return self.x

        def c():
            if c_v.get() == 'No':
                self.GA.config(state="disable")
                self.x =  1
            else:
                self.GA.config(state="normal")
                self.x = 0
            return self.x
        

        v = tk.StringVar()
        def SetText (totalValue):
            v.set(totalValue)  


        def KnapsackAlgorithm():
           if weigthCheck():
                  messagebox.showerror("!!!!!!", "PlEASE, enter a weigth greater than 125 :)")
           else:
                   ChoosedIndiv = SelectedAlgorithm()
                   TotalValue = 0
                    
                   w1 = tk.StringVar()
                   def Setnum1 (index):
                          w1.set(index)
                     
                   w2 = tk.StringVar()
                   def Setnum2 (index):
                          w2.set(index)

                   w3 = tk.StringVar()
                   def Setnum3 (index):
                          w3.set(index)

                   w4 = tk.StringVar()
                   def Setnum4 (index):
                          w4.set(index)

                   w5 = tk.StringVar()
                   def Setnum5 (index):
                          w5.set(index)

                   w6 = tk.StringVar()
                   def Setnum6 (index):
                          w6.set(index)


                   for x in range(len(ChoosedIndiv)):

                        if ChoosedIndiv[x]==0:
                            itemIndex0 = x

                            if itemIndex0 == 0:
                               self.item1.configure(background="#d50000")
                               self.Entry1.configure(textvariable="0")
                        
                            if itemIndex0 == 1:
                               self.item2.configure(background="#d50000")
                               self.Entry2.configure(textvariable="0")
                        
                            if itemIndex0 == 2:
                               self.item3.configure(background="#d50000")
                               self.Entry3.configure(textvariable="0")

                            if itemIndex0 == 3:
                               self.item4.configure(background="#d50000")
                               self.Entry4.configure(textvariable="0")
                        
                            if itemIndex0 == 4:
                               self.item5.configure(background="#d50000")
                               self.Entry5.configure(textvariable="0")
                        
                            if itemIndex0 == 5:
                               self.item6.configure(background="#d50000")
                               self.Entry6.configure(textvariable="0")
                        else :
                        

                          itemIndex1 = x

                          TotalValue =(TotalValue+ items[itemIndex1][1]*ChoosedIndiv[itemIndex1])
                          if itemIndex1 == 0:
                             Setnum1(ChoosedIndiv[itemIndex1])
                             self.item1.configure(background="#8bc34a")
                             self.Entry1.configure(textvariable=w1)
                        
                          if itemIndex1 == 1:
                             Setnum2(ChoosedIndiv[itemIndex1])
                             self.Entry2.configure(textvariable=w2)
                             self.item2.configure(background="#8bc34a")
                        
                          if itemIndex1 == 2:
                             Setnum3(ChoosedIndiv[itemIndex1])
                             self.Entry3.configure(textvariable=w3)
                             self.item3.configure(background="#8bc34a")

                          if itemIndex1 == 3:
                             Setnum4(ChoosedIndiv[itemIndex1])
                             self.Entry4.configure(textvariable=w4)
                             self.item4.configure(background="#8bc34a")
                        
                          if itemIndex1 == 4:
                             Setnum5(ChoosedIndiv[itemIndex1])
                             self.Entry5.configure(textvariable=w5)
                             self.item5.configure(background="#8bc34a")
                        
                          if itemIndex1 == 5:
                             Setnum6(ChoosedIndiv[itemIndex1])
                             self.Entry6.configure(textvariable=w6)
                             self.item6.configure(background="#8bc34a")
           return TotalValue


        def Run():
            try :
                TotalValue = KnapsackAlgorithm()
                TotalValue = SetText(TotalValue)
                self.totalValueNum.configure(textvariable=v)
            except :
                messagebox.showerror("!!!!!!", "PLEASE, enter a weigth for knapsack and make a selection :)")


        def Back():
            FirstScreen_support.destroy_window()
            import FirstScreen
            FirstScreen.vp_start_gui()
 
        self.startBtn = tk.Button(top)
        self.startBtn.place(relx=0.870, rely=0.04, height=34, width=57)
        self.startBtn.configure(background="#dcedc8")
        self.startBtn.configure(borderwidth="3")
        self.startBtn.configure(font="-family {System} -size 10 -weight bold")
        self.startBtn.configure(text='''Start''')
        self.startBtn.configure(command=Run)

        self.knapsackFram = tk.LabelFrame(top)
        self.knapsackFram.place(relx=0.033, rely=0.156, relheight=0.744 , relwidth=0.933)
        self.knapsackFram.configure(relief='groove')
        self.knapsackFram.configure(borderwidth="4")
        self.knapsackFram.configure(font="-family {System} -size 10 -weight bold")
        self.knapsackFram.configure(text='''Knapsack''')
        self.knapsackFram.configure(background="#dcedc8")

        self.item1 = tk.Button(self.knapsackFram)
        self.item1.place(relx=0.839, rely=0.119, height=34, width=60
               , bordermode='ignore')
        self.item1.configure(background="#d50000")
        self.item1.configure(cursor="hand2")
        self.item1.configure(font="-family {System} -size 10 -weight bold")
        self.item1.configure(text=format(items[0]))

        self.item2 = tk.Button(self.knapsackFram)
        self.item2.place(relx=0.839, rely=0.269, height=34, width=60
                , bordermode='ignore')
        self.item2.configure(cursor="hand2")
        self.item2.configure(background="#d50000")
        self.item2.configure(font="-family {System} -size 10 -weight bold")
        self.item2.configure(text=format(items[1]))

        self.item3 = tk.Button(self.knapsackFram)
        self.item3.place(relx=0.839, rely=0.418, height=34, width=60
               , bordermode='ignore')
        self.item3.configure(background="#d50000")
        self.item3.configure(cursor="hand2")
        self.item3.configure(font="-family {System} -size 10 -weight bold")
        self.item3.configure(text=format(items[2]))

        self.item4 = tk.Button(self.knapsackFram)
        self.item4.place(relx=0.839, rely=0.567, height=34, width=60
                 , bordermode='ignore')
        self.item4.configure(background="#d50000")
        self.item4.configure(font="-family {System} -size 10 -weight bold")
        self.item4.configure(text=format(items[3]))

        self.item5 = tk.Button(self.knapsackFram)
        self.item5.place(relx=0.839, rely=0.716, height=34, width=60
                 , bordermode='ignore')
        self.item5.configure(background="#d50000")
        self.item5.configure(font="-family {System} -size 10 -weight bold")
        self.item5.configure(text=format(items[4]))

        self.item6 = tk.Button(self.knapsackFram)
        self.item6.place(relx=0.839, rely=0.866, height=34, width=60
                , bordermode='ignore')
        self.item6.configure(background="#d50000")
        self.item6.configure(font="-family {System} -size 10 -weight bold")
        self.item6.configure(text=format(items[5]))

        self.totalValue = tk.Label(self.knapsackFram)
        self.totalValue.place(relx=0.036, rely=0.750, height=21, width=84
                , bordermode='ignore')
        self.totalValue.configure(background="#dcedc8")
        self.totalValue.configure(font="-family {System} -size 10 -weight bold")
        self.totalValue.configure(text='''Total Value''')

        self.totalValueNum = tk.Entry(self.knapsackFram)
        self.totalValueNum.place(relx=0.054, rely=0.800, height=30
                , relwidth=0.150, bordermode='ignore')
        self.totalValueNum.configure(background="white")
        self.totalValueNum.configure(borderwidth="2")
        self.totalValueNum.configure(font="-family {System} -size 10 -weight bold")

        self.Label5 = tk.Label(self.knapsackFram)
        self.Label5.place(relx=0.255, rely=0.098, height=247, width=229
                , bordermode='ignore')
        self.Label5.configure(background="#dcedc8")
        photo_location = os.path.join(prog_location,"knapsack.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label5.configure(image=_img0)
        self.Label5.configure(text='''Label''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.083, rely=0.911, height=21, width=24)
        self.Label1.configure(background="#d50000")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.15, rely=0.911, height=21, width=74)
        self.Label2.configure(background="#dcedc8")
        self.Label2.configure(font="-family {System} -size 10 -weight bold")
        self.Label2.configure(text='''Unpacked''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.367, rely=0.911, height=21, width=24)
        self.Label3.configure(background="#8bc34a")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.433, rely=0.911, height=21, width=84)
        self.Label4.configure(background="#dcedc8")
        self.Label4.configure(font="-family {System} -size 10 -weight bold")
        self.Label4.configure(text='''Packed''')

        self.Label6 = tk.Label(self.knapsackFram)
        self.Label6.place(relx=0.810, rely=0.03, height=21, width=100
                 , bordermode='ignore')
        self.Label6.configure(background="#dcedc8")
        self.Label6.configure(font="-family {System} -size 10 -weight bold")
        self.Label6.configure(text='''(Weigth , Value)''')

        self.Entry1 = tk.Entry(self.knapsackFram)
        self.Entry1.place(relx=0.790, rely=0.119, height=20, relwidth=0.037
                   , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="-family {System} -size 10 -weight bold")

        self.Entry2 = tk.Entry(self.knapsackFram)
        self.Entry2.place(relx=0.790, rely=0.269, height=20, relwidth=0.037
                   , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="-family {System} -size 10 -weight bold")

        self.Entry3 = tk.Entry(self.knapsackFram)
        self.Entry3.place(relx=0.790, rely=0.418, height=20, relwidth=0.037
                   , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="-family {System} -size 10 -weight bold")

        self.Entry4 = tk.Entry(self.knapsackFram)
        self.Entry4.place(relx=0.790, rely=0.567, height=20, relwidth=0.037
                   , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="-family {System} -size 10 -weight bold")

        self.Entry5 = tk.Entry(self.knapsackFram)
        self.Entry5.place(relx=0.790, rely=0.716, height=20, relwidth=0.037
                   , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="-family {System} -size 10 -weight bold")
        self.Entry6 = tk.Entry(self.knapsackFram)
        self.Entry6.place(relx=0.790, rely=0.866, height=20, relwidth=0.037
                   , bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="-family {System} -size 10 -weight bold")

        self.GA = tk.Checkbutton(top)
        self.GA.place(relx=0.400, rely=0.022, relheight=0.056
                    , relwidth=0.400)
        self.GA.configure(background="#dcedc8")
        self.GA.configure(font="-family {System} -size 10 -weight bold")
        self.GA.configure(justify='left')
        self.GA.configure(text='''Genetic Algorithm''')
        self.GA.configure(variable=c_v) 
        self.GA.configure(onvalue='Yes', offvalue='')
        self.GA.configure(command=check)

        self.DE = tk.Checkbutton(top)
        self.DE.place(relx=0.400, rely=0.077, relheight=0.056
                   , relwidth=0.400)
        self.DE.configure(background="#dcedc8")
        self.DE.configure(font="-family {System} -size 10 -weight bold")
        self.DE.configure(foreground="#000000")
        self.DE.configure(text='''Differential Evalution''')
        self.DE.configure(variable=c_v) 
        self.DE.configure(onvalue='No', offvalue='')
        self.DE.configure(command=c)

        self.backBtn = tk.Button(top)
        self.backBtn.place(relx=0.0, rely=0.0, height=24, width=47)
        self.backBtn.configure(font="-family {System} -size 10 -weight bold")
        self.backBtn.configure(background="#dcedc8")
        self.backBtn.configure(command=Back)
        self.backBtn.configure(text='''Back''')