class Atm:

    #Static/Class Variable : Have same value for all obj
    __counter=0

    def __init__(self):

    # .pin is public
    # ._pin is protected 
    # .__pin is private 
    # Encapsulation is used to protect your data
    # Private attibutes can be data as well as methods.
    # Instance Variables : Which have diff value for each obj

        self.__pin=""
        self.__balance=0
        self.sno=Atm.__counter
        Atm.__counter+=1

        self.__menu()

    def __menu(self):
        user_input=input("""
            1.ENTER 1 TO SET pin
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

    # Getter and Setter are made to encapsulate some information from the user so that no unwanted modification is carried out over data+mehtods of a particular class.
    # Its not like private ata cannot be accessed (_class__method e.g. _Atm__pin) by this they can be accessed but not preffered.
    # self is not used in static methods as they are not referenced with an obj of class, they are irrespective of obj.
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter==new
        else:
            print("Not Allowed")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin Changed")
        else:
            print("Not Allowed")

    def pin_set(self):
        self.__pin=input("Enter your pin: ")
        print("Pin set Successfully")
        self.__menu()
    
    def deposit_amount(self):
        temp=input("Enter your pin: ")
        if temp==self.__pin:
            amount=int(input("Enter amount to deposit: "))
            self.__balance+=amount
            print(f"Deposit Successful,Balance {self.__balance}")
        else:
            print("Pin Incorrect")
        self.__menu()
    
    def withdraw_amount(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            amount=int(input("Enter amount to withdraw: "))
            if amount<self.__balance:
                self.__balance-=amount
                print(f"Withdraw Successful,Balance {self.__balance}")
            else:
                print("Withdraw amount exceeded you account balance")
        else:
            print("Pin Incorrect")
        self.__menu()
    
    def show_balance(self):
        print(f"Account balance is {self.__balance}")
        self.__menu()

# khushi is a reference variable which is pointing to a object of Atm class
khushi=Atm()


    