# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default"
    @classmethod
    def change_bank_name(cls, name): cls.bank_name = name

a, b = Bank(), Bank()
print(a.bank_name, b.bank_name) 
Bank.change_bank_name("New")
print(a.bank_name, b.bank_name)  