def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

class BankHolder():
    def __init__(self,starting_amount=0):
        self.balance = starting_amount
    
    def deposit(self,amount):
        self.balance +=amount
        
    def withdraw(self,amount):
        self.balance -=amount
    
    def collect_interest(self):
        self.balance *=1.1
        
    
    