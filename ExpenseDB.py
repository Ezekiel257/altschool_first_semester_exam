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

class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id):
        return next((expense for expense in self.expenses if expense.id == expense_id), None)

    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

# Sample usage:
expense_db = ExpenseDB()

expense1 = Expense("Groceries", 50.0)
expense2 = Expense("Rent", 1200.0)

expense_db.add_expense(expense1)
expense_db.add_expense(expense2)

print("All Expenses:")
print(expense_db.to_dict())

print("\nRemoving an Expense:")
expense_db.remove_expense(expense1.id)
print(expense_db.to_dict())

print("\nGetting Expense by ID:")
print(expense_db.get_expense_by_id(expense2.id).to_dict() if expense_db.get_expense_by_id(expense2.id) else "Expense not found")

print("\nGetting Expenses by Title:")
print(expense_db.get_expenses_by_title("Rent"))
