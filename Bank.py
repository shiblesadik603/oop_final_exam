# Bank Management System
class Bank:
    bankname="Jonota Bank"
    branch="KUET,Khulna,Bangladesh"

    def __init__(self):
        # self.bankname=bankname
        # self.branch=branch
        self.bank_balance=0.0
        self.All_Account={}
        self.Transactions = {}

    # create account
    def create_account(self,username,ID,address,user_balance):
        self.username=username
        self.ID=ID
        self.address=address
        self.user_balance=user_balance
        self.All_Account[ID]={'Name':username,'Address':address,'Balance':user_balance}
        print(f'Hello {self.username} congratulations! your account created successfully.')
        self.bank_balance=self.bank_balance+user_balance
        
    # deposit
    def deposit(self,amount,ID_num):
        p=0
        for k,v in self.All_Account.items():
            if k==ID_num:
                v['Balance']=v['Balance']+amount
                self.bank_balance=self.bank_balance + amount
                print(f'{amount} deposit successfully from {k}.')
                # self.Transactions[k].append('f"{amount} deposit successfully from {k}."')
                # target_list=self.Transactions[k]
                # target_list.append(f'{amount} deposit successfully')
                p=1
        if p==0:
            print('Your ID number is wrong, Check it again.')
            
    # withdraw
    def withdraw(self,amount,ID_num):
        p=0
        for k,v in self.All_Account.items():
            if k==ID_num:
                if v['Balance']>amount:
                    v['Balance']=v['Balance']-amount
                    self.bank_balance=self.bank_balance-amount
                    print(f'{amount} withdraw successfully from {k}.')
                else:
                    print('Insufficient fund...')
                p=1
        if p==0:
            print('Your ID number is wrong, Check it again.')

    # ministatement
    def Accounts_Details(self):
        for k, v in self.All_Account.items():
            print(k, v['Name'], v['Address'],v['Balance']) 

    # Balance
    def Check_Balance(self,ID_num):
        for k,v in self.All_Account.items():
            if k==ID_num:
                print(v['Name'],v['Balance'])

    # Transfer Money
    def transfer_money(self,ID_num1,ID_num2,amount):
        for k,v in self.All_Account.items():
            if k==ID_num1:
                if v['Balance']>amount:
                    self.withdraw(amount,ID_num1)
                    self.deposit(amount,ID_num2)
                else:
                    print('Your ID number is wrong, Check it again.')

    # Transactions
    def transaction(self):
        # for key,data in Transactions.items():
        #     print(f"key: {key}")
        #     for info in data:
        #         print(info)
        for key,data in self.Transactions.items():
            print(data) 

    # Bank Money
    def Bank_Money(self):
        amount=self.bank_balance
        print(amount)
        return amount
    
class User:

    def loan(self,amount):
        bank=Bank()
        a=bank.Bank_Money()
        print(a)
        c=input('Enter Yes or No: ')
        loan=0.0
        if c=="Yes":
            print(a)
            if amount < a:
                loan=loan+amount
                a=a-amount
            else:
                print('Bank can not give you the loan.')
        else:
            print('There are no option to give you the loan.')

print(f'Welcome to {Bank.bankname} , {Bank.branch}')

from Bank import Bank
from User import User

def main():
    b=Bank()
    c=User()

    while True:
        print('Please select your desire option.')
        print('1.Create Account')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Accounts Details')
        print('5.Available_Balance')
        print('6.Transfer_Money')
        print('7.Transactions')
        print('8.Bank_Balance')
        print('9.Loan')
        print('10.Stop')
        option=int(input(''))

        if option==1:
            username=input('Enter your name : ')
            ID=int(input('Enter ID number : '))
            address=input('Enter your address : ' )
            user_balance=float(input('What is the amount of money you want to deposit first : '))
            b.create_account(username,ID,address,user_balance)
        # All_Account[ID]={'Name':username,'Address':address,'Balance':user_balance}

        elif option==2:
            amount=float(input('Enter Deposited Amount : '))
            ID_num=int(input('Enter your ID number : '))
            b.deposit(amount,ID_num)

        elif option==3:
            amount=float(input('Enter withdraw Amount : '))
            ID_num=int(input('Enter your ID number : '))
            b.withdraw(amount,ID_num)

        elif option==4:
            b.Accounts_Details()

        elif option==5:
            ID_num=int(input('Enter your ID number : '))
            x=b.Check_Balance(ID_num)

        elif option==6:
            ID_num1=int(input('Enter your ID number : '))
            ID_num2=int(input('Enter the ID number where you want to transfer : '))
            amount=float(input('Enter Amount : '))
            b.transfer_money(ID_num1,ID_num2,amount)
    
        elif option==7:
            b.transaction()

        elif option==8:
            b.Bank_Money()

        elif option==9:
            q=float(input('Enter amount: '))
            c.loan(q)

        elif option==10:
            print('Thanks for using Jonota Bank services... ')
            break

if __name__=='__main__':
    main()