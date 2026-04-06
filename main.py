from bank_account import BankAccount
from validators import RatingValidator

def run_bank_demo():
    acc=BankAccount("Mateen",1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc)

def run_validator_demo():
    data=[1,2,3,6,None]
    validator = RatingValidator('rating')
    validator.validate(data)
    print("Valid: ", validator.is_valid)
    print("Error: ",validator.errors)

if __name__=='__main__':
    run_bank_demo()
    run_validator_demo()