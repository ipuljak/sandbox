from src.constants.tax_rates import TAX_RATE_CANADA_FEDERAL_2019, TAX_RATE_CANADA_ONTARIO_2019
from src.utils.format import format_currency

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

        return self.calculate_tax(TAX_RATE_CANADA_FEDERAL_2019) + self.calculate_tax(TAX_RATE_CANADA_ONTARIO_2019)


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
            format_currency(self.income),
            format_currency(self.calculate_net_income()),
            format_currency(self.calculate_total_tax()),
            format_currency(self.calculate_monthly_income(True))
        )
