from tkinter import *

class Calculator:

    def __init__(self):

        self.root=Tk()

        self.root.title('Basic Calculator')

        self.root.minsize(210,322)
        self.root.maxsize(250,450)

        self.result=Label(self.root,text='',bg='white',width=6, height=2)
        self.result.grid(row=0,column=0)

        self.btn1=Button(self.root,text='1',bg='pink',width='6',height=4, command=lambda: self.get_num("1")).grid(row=1,column=0)
        self.btn2=Button(self.root,text='2',bg='pink',width='6',height=4, command=lambda: self.get_num("2")).grid(row=1,column=1)
        self.btn3=Button(self.root,text='3',bg='pink',width='6',height=4, command=lambda: self.get_num("3")).grid(row=1,column=2)
        self.btnAdd=Button(self.root,text='+',bg='cyan',width='6',height=4, command=lambda: self.get_operator("+")).grid(row=1,column=3)

        self.btn4=Button(self.root,text='4',bg='pink',width='6',height=4, command=lambda: self.get_num("4")).grid(row=2,column=0)
        self.btn5=Button(self.root,text='5',bg='pink',width='6',height=4, command=lambda: self.get_num("5")).grid(row=2,column=1)
        self.btn6=Button(self.root,text='6',bg='pink',width='6',height=4, command=lambda: self.get_num("6")).grid(row=2,column=2)
        self.btnSubt=Button(self.root,text='-',bg='cyan',width='6',height=4, command=lambda: self.get_operator("-")).grid(row=2,column=3)

        self.btn7=Button(self.root,text='7',bg='pink',width='6',height=4, command=lambda: self.get_num("7")).grid(row=3,column=0)
        self.btn8=Button(self.root,text='8',bg='pink',width='6',height=4, command=lambda: self.get_num("8")).grid(row=3,column=1)
        self.btn9=Button(self.root,text='9',bg='pink',width='6',height=4, command=lambda: self.get_num("9")).grid(row=3,column=2)
        self.btnDiv=Button(self.root,text='/',bg='cyan',width='6',height=4, command=lambda: self.get_operator("/")).grid(row=3,column=3)

        self.btn0=Button(self.root,text='0',bg='pink',width='6',height=4, command=lambda: self.get_num("0")).grid(row=4,column=0)
        self.btnClr=Button(self.root,text='C',bg='pink',width='6',height=4, command=lambda: self.clear()).grid(row=4,column=1)
        self.btnMul=Button(self.root,text='*',bg='cyan',width='6',height=4, command=lambda: self.get_operator("*")).grid(row=4,column=2)
        self.btnEquals=Button(self.root,text='=',bg='blue',width='6',height=4, command=lambda: self.get_result()).grid(row=4,column=3)
        self.root.mainloop()

    def get_num(self,num):

        new_text=self.result['text']+num
        self.result.configure(text=new_text)

    def clear(self):

        self.result.configure(text="")

    def get_operator(self,opr):

        self.first_num=int(self.result['text'])
        self.result.configure(text="")
        self.operator=opr

    def get_result(self):

        self.second_num=int(self.result['text'])

        if self.operator=='+':
            result=self.first_num + self.second_num
        elif self.operator=='-':
            result=self.first_num - self.second_num
        elif self.operator=='*':
            result=self.first_num * self.second_num
        else:
            if self.second_num==0:
                self.configure(text="Gadhe")
            else:
                result=self.first_num / self.second_num
        self.result.configure(text=str(result))

obj=Calculator()

















