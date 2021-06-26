class Income:

    def __init__(self, amount, tax = 4):
        self.amount = amount
        self.set_tax(tax)

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        if(amount < 0):
            raise ValueError("Amount of income can not be less than Zero.")
        self.amount = amount

    def get_tax(self):
        return self.tax

    def set_tax(self, tax):
        if(tax < 0):
            raise ValueError("tax of income can not be less than Zero.")

        if(tax > 20):
            raise ValueError("tax of income can not be greater than 20.")
        self.tax = tax

    amount = property()
    # tax = property()

income = Income(500,3)

print(income.amount)