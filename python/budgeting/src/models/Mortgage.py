import math
from src.utils.format import format_currency

class Mortgage:
    """Mortgage class."""

    def __init__(self, amount, down, interest, amortization):
        """
        Craete a new mortgage class.

        :param str amount: Total cost of the property
        :param int down: Down payment
        :param float interest: Interest rate (format: 3.64 for 3.64% interest rate)
        :param int amortization: Number of years on the mortgage
        """

        self.amount = amount
        self.down = down
        self.interest = interest
        self.amortization = amortization


    def get_principal(self):
        """Calculate the principle on the loan."""

        return self.amount - self.down


    def get_number_of_payments(self):
        """Calcualte the total number of payments on the loan."""

        return self.amortization * 12


    def get_monthly_interest_rate(self):
        """Calculate the monthly interest rate."""

        return (self.interest / 100) / 12


    def get_mortgage_payment(self):
        """Calculate the mortgage monthly payment."""

        p = self.get_principal()
        n = self.get_number_of_payments()
        r = self.get_monthly_interest_rate()

        # Fancy mortgage formula
        m = p * ((r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))

        return round(m, 2)


    def __repr__(self):
        return "<Mortgage amount:%s down:%s interest:%s amortization:%s" % \
            (self.amount, self.down, self.interest, self.amortization)


    def __str__(self):
        return """Mortage:
        Total cost - {}
        Down payment - {}
        Principal - {}
        Interest rate - {}%
        Amortization - {} year(s)
        Mortgage payment - {}
        """.format(
            format_currency(self.amount),
            format_currency(self.down),
            format_currency(self.get_principal()), 
            self.interest, 
            self.amortization, 
            format_currency(self.get_mortgage_payment()))
     