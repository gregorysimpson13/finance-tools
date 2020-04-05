class Debt:
    def __init__(self, balance, apr, name, min_payment):
        self.__balance = float(balance)
        self.__apr = float(apr)
        self.__name = name
        self.__min_payment = float(min_payment)
        self.__interest = 0
        self.__payments = 0

    def roll_over_interest(self):
        if self.is_paid_off():
            return
        interest = round(self.__apr / 12 * 0.01 * self.__balance, 2)
        self.__interest = self.__interest + interest
        self.__balance = self.__balance + interest
    
    # return leftover payment
    def make_payment(self, payment):
        if payment > self.__balance:
            self.__balance = 0
            return payment - self.__balance
        self.__balance -= payment
        return 0

    def minimum_payment(self):
        minimum_payment = self.get_minimum_payment()
        if minimum_payment == 0:
            return 0
        self.__balance = self.__balance - minimum_payment
        self.__payments += 1
        return minimum_payment

    def is_paid_off(self):
        return self.__balance == 0

    def get_balance(self):
        return self.__balance

    def get_apr(self):
        return self.__apr

    def get_name(self):
        return self.__name

    def get_interest(self):
        return self.__interest

    def get_payments(self):
        return self.__payments

    def get_minimum_payment(self):
        if self.__min_payment < self.__balance:
            return self.__min_payment
        else:
            return self.__balance

    
