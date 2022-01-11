class Bank_account():
    
    def __init__(self):
        self.number = "12 3456 5555 9090 1111 0000 7722"
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount2):
        if amount2 <= self.balance:
            self.balance -= amount2
        else:
            print("Insufficient funds on the account\n")
    
    def display_info(self):
        print(f"Bank Account No: {self.number}\nBalance: PLN {self.balance}\n")
 

bank = Bank_account()       
bank.display_info()
bank.deposit(25.30)
bank.display_info()
bank.withdraw(31.70)
bank.display_info()
bank.withdraw(14)
bank.display_info()