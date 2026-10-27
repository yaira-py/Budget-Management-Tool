import tkinter as tk
from tkinter import ttk

class BudgetManagement:
    def __init__(self,root):
        self.root=root
        self.root.title('Management')
        self.root.geometry('500x550')
        self.root.configure(bg="#f3eeee")

        self.expenses=[]
        self.total=0.0

        self.title=tk.Label(self.root,text='Budget Management Tool',font=('Arial',15,'bold'),fg='black',bg='#f3eeee')
        self.title.pack(pady=10)

        self.income_lb=tk.Label(self.root,text='Income:',font=('Arial',11),fg='grey',bg='#f3eeee')
        self.income_lb.pack(pady=(10,0),anchor='sw',padx=30,)

        self.income_entry=tk.Entry(self.root,width=28)
        self.income_entry.pack(pady=5,ipady=4,fill='x',padx=30)


        self.expense_lb=tk.Label(self.root,text='Expense Amount:',font=('Arial',11),fg='grey',bg='#f3eeee')
        self.expense_lb.pack(pady=(10,0),anchor='sw',padx=30)

        self.expense_entry=tk.Entry(self.root,width=28)
        self.expense_entry.pack(pady=5,ipady=4,fill='x',padx=30)

        
        self.category_lb=tk.Label(self.root,text='Expense Category:',font=('Arial',11),fg='grey',bg='#f3eeee')
        self.category_lb.pack(pady=(10,0),anchor='sw',padx=30)

        self.category=ttk.Combobox(self.root,values=['Utilities','Food','Rent','Transport','Shopping'])
        self.category.set('Food')
        self.category.pack(pady=5,ipady=4,fill='x',padx=30)

        self.expense_btn=tk.Button(self.root,text='Add Expense',font=('Arial',13,'bold'),bg="#2777B8",fg='white',
                             command=self.add_expense )
        self.expense_btn.pack(pady=10,fill='x',padx=30,ipady=3)

        self.list_lb=tk.Label(self.root,text='Utilities: $00.0',bg='#f3eeee',fg='black',font=('Arial',11))
        self.list_lb.pack(pady=10,padx=30,anchor='sw')

        self.frame=tk.Frame(self.root,bg='#f3eeee')
        self.frame.pack(padx=20,fill='x',pady=5)
        tk.Label(self.frame,text='Total Expense:',font=('Arial',11),fg='grey',bg='#f3eeee').pack(side='left',padx=10)

        self.total_lb=tk.Label(self.frame,text='00.0',font=('Arial',11),fg='grey',bg='#f3eeee')
        self.total_lb.pack(side='right',padx=10)

        self.cal_btn=tk.Button(self.root,text='Calculate',font=('Arial',13,'bold'),bg="#2EA742",fg='white',
                                   command=self.Calculate)
        self.cal_btn.pack(pady=15,fill='x',padx=30,ipady=3)

        self.saving_lb=tk.Label(self.root,text='Savings: $-',bg='#f3eeee',fg='grey',font=('Arial',11))
        self.saving_lb.pack(pady=10,anchor='sw',padx=30)


    def add_expense(self):
        try:
            amount=float(self.expense_entry.get())
            cat=self.category.get()
            self.expenses.append((cat,amount))
            self.total+=amount

            text= ' , '.join([f'{c}: ${a:.2f}' for c,a in self.expenses])
            self.list_lb.config(wraplength=350,justify='left')
            self.list_lb.config(text=text)
            self.total_lb.config(text=f'{self.total:.2f}')
            self.expense_entry.delete(0,tk.END)

        except:
            pass


    def Calculate(self):
        try:
            income=float(self.income_entry.get())
            saving=income-self.total
            self.saving_lb.config(text=f'Savings: ${saving:.2f}')

        except:
            self.saving_lb.config(text='Savings: Enter Valid Income')





if __name__=='__main__':
    window=tk.Tk()
    app=BudgetManagement(window)
    window.mainloop()
