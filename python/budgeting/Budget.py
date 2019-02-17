import math
import utils

class Budget(object):
    """Budget calculator."""

    def __init__(self):
        self.people = []
        self.mortgage = None


    def add_income(self, person):
        """Add a new income to the budget."""

        self.people.append(person)


    def get_total_savings(self):
        """Return the total savings between all of the incomes in the budget."""

        return sum(p.savings for p in self.people)


    def get_total_income(self, net=False):
        """Return the total monthly income between all of the incomes in the budget."""

        if net:
            return sum(i.income.calculate_net_income() for i in self.people)

        return sum(i.income.income for i in self.people)


    def get_total_monthly_income(self, net=False):
        """Return the total monthly income between all of the incomes in the budget."""

        return sum(i.income.calculate_monthly_income(net) for i in self.people)


    def add_mortgage(self, mortgage):
        """Add a mortgage to the budget."""

        self.mortgage = mortgage


    def calculate_mortgage_affordability(self):
        """Calculate the mortgage affordability."""

        if not self.mortgage:
            raise ValueError("Budget has no mortgage set!")

        return round((self.mortgage.get_mortgage_payment() / self.get_total_monthly_income(True)) * 100, 2)


    def __str__(self):
        return """Budget:
        Total savings - {}
        Total income - {}
        Total net income - {}
        Total monthly income - {}
        Total net monthly income - {}
        Mortgage monthly payment percetage - {}%
        """.format(
            utils.pretty_print_currency(self.get_total_savings()),
            utils.pretty_print_currency(self.get_total_income()),
            utils.pretty_print_currency(self.get_total_income(True)),
            utils.pretty_print_currency(self.get_total_monthly_income()),
            utils.pretty_print_currency(self.get_total_monthly_income(True)),
            self.calculate_mortgage_affordability()
        )
