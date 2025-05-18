import threading
import time

# Base class using Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    # Withdraw method is thread-safe
    def withdraw(self, amount):
        # with self.lock:
            if self.balance >= amount:
                print(f"{threading.current_thread().name} is withdrawing {amount} and current balance is Balance: {self.balance}")
                time.sleep(1)
                self.balance -= amount
                print(f"{threading.current_thread().name} completed. Balance: {self.balance}")
            else:
                print(f"{threading.current_thread().name} tried to withdraw {amount}, but insufficient balance!")

# Subclass demonstrating Inheritance and Polymorphism
class FastWithdrawal(BankAccount):
    def withdraw(self, amount):
        print(f"{threading.current_thread().name} doing fast withdrawal")
        super().withdraw(amount)

# Shared account
account = FastWithdrawal(1000)

# Threads trying to withdraw
t1 = threading.Thread(target=account.withdraw, args=(600,), name="User1")      #☝️ account.withdraw only no bracket   args=(600,) comma must
t2 = threading.Thread(target=account.withdraw, args=(600,), name="User2")

t1.start()
t2.start()

t1.join()
t2.join()
