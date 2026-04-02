class Atm:

    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input("""
            1.ENTER 1 TO SET PIN
            2.ENTER 2 TO DEPOSIT MONEY
            3.ENTER 3 TO WITHDRAW MONEY
            4.ENTER 4 TO CHECK BALANCE
            5.ENTER 5 TO EXIT
              """)
        
        if user_input=="1":
            self.pin_set()
        elif user_input=="2":
            self.deposit_amount()
        elif user_input=="3":
            self.withdraw_amount()
        elif user_input=="4":
            self.show_balance()
        else:
            print("bye")

    def pin_set(self):
        self.pin=input("Enter your pin: ")
        print("Pin set Successfully")
        self.menu()
    
    def deposit_amount(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter amount to deposit: "))
            self.balance+=amount
            print(f"Deposit Successful,Balance {self.balance}")
        else:
            print("Pin Incorrect")
        self.menu()
    
    def withdraw_amount(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            amount=int(input("Enter amount to withdraw: "))
            if amount<self.balance:
                self.balance-=amount
                print(f"Withdraw Successful,Balance {self.balance}")
            else:
                print("Withdraw amount exceeded you account balance")
        else:
            print("Pin Incorrect")
        self.menu()
    
    def show_balance(self):
        print(f"Account balance is {self.balance}")
        self.menu()


khushi=Atm()


    
