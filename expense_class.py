#Represents an individual financial expense.

from uuid import uuid4
from datetime import datetime, timezone
import random

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Predefined expense titles
predefined_titles = ["Groceries", "Furnitures", "Electronics", "Clothing", "Books", "Home Decor", "Appliances", "Toys", "Sports Gear", "Stationery"]

# Generate up to 20 randomly created Expense instances
expenses = []
for _ in range(20):
    title = random.choice(predefined_titles)
    amount = round(random.uniform(1.0, 100.0), 2)
    expense = Expense(title, amount)
    expenses.append(expense)

# Print the generated expenses
for i, expense in enumerate(expenses, start=1):
    print(f"Expense {i}: {expense.to_dict()}")

# Sample usage:
expense1 = Expense("Groceries", 50.0)
expense2 = Expense("Utensils", 60.0)

print(expense1.to_dict())
print(expense2.to_dict())

# Updating the expense
expense1.update(amount=55.0)
print(expense1.to_dict())











