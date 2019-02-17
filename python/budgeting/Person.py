import utils

class Person:
    """Person class."""

    def __init__(self, first, last, age, savings, income):
        self.first = first
        self.last = last
        self.age = age
        self.savings = savings
        self.income = income

    
    def __str__(self):
        return """Person:
        Name - {}
        Age - {}
        Income - {}
        Net income - {}
        Tax - {}
        After tax monthly income - {}
        """.format(
            "{} {}".format(self.first, self.last),
            self.age,
            utils.pretty_print_currency(self.income.income),
            utils.pretty_print_currency(self.income.calculate_net_income()),
            utils.pretty_print_currency(self.income.calculate_total_tax()),
            utils.pretty_print_currency(self.income.calculate_monthly_income(True))
        )
