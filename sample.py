balance=1000

try:
    print("Withdraw Money")
    amount=int(input("Enter amount to withdraw: "))
    if balance>=amount:
        balance=balance-amount
except:
    print("cljhg")
    
finally:
    balance=balance-10


print(balance)

