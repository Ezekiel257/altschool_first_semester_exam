#Represents an individual financial expense.

from uuid import uuid4
from datetime import datetime, timezone

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

# Sample usage:
expense1 = Expense("Groceries", 50.0)
print(expense1.to_dict())

# Updating the expense
expense1.update(amount=55.0)
print(expense1.to_dict())









