import utils

FEDERAL_TAX_RATE = [(47630, .15), (47629, .205), (52408, .26), (62704, .29), (210371, .33)]
ONTARIO_TAX_RATE = [(43906, .0505), (43907, .0915), (62187, .1116), (70000, .1216), (220000, .1316)]

class Income(object):
    """Income class."""
    
    def __init__(self, income):
        self.income = income


    def calculate_tax(self, rates):
        """Calculate the income tax based on the given rates.
        Rates is a list of tuples in the format of (amount, rate)."""

        tax = 0
        remaining = self.income

        for rate in rates:
            taxable = min(remaining, rate[0])
            tax += taxable * rate[1]
            remaining -= taxable

            if remaining == 0:
                return tax


    def calculate_total_tax(self):
        """Calculate the total tax based on 2019 Canadian Federal + Ontario tax rates."""

        return self.calculate_tax(FEDERAL_TAX_RATE) + self.calculate_tax(ONTARIO_TAX_RATE)


    def calculate_net_income(self):
        """Calculate the net income after tax."""

        return self.income - self.calculate_total_tax()


    def calculate_monthly_income(self, net=False):
        """Calculate the income per month. 

        :param bool net: True if after tax, False if before tax"""

        income = self.calculate_net_income() if net else self.income

        return income / 12
        

    def __str__(self):
        return """Income:
        Income - {}
        Net income - {}
        Tax - {}
        After tax monthly income - {}
        """.format(
            utils.pretty_print_currency(self.income),
            utils.pretty_print_currency(self.calculate_net_income()),
            utils.pretty_print_currency(self.calculate_total_tax()),
            utils.pretty_print_currency(self.calculate_monthly_income(True))
        )
