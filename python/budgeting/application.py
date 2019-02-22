from src.models.Budget import Budget
from src.models.Income import Income
from src.models.Mortgage import Mortgage
from src.models.Person import Person

ivan = Person("Ivan", "Puljak", 27, 10000, Income(40000))

mortgage = Mortgage(200000, 70000, 3.64, 25)

budget = Budget()
budget.add_income(ivan)
budget.add_mortgage(mortgage)

print(ivan)
print(mortgage)
print(budget)