# Altschool First Semester Exam

## Project Description
This project implements two classes, `Expense` and `ExpenseDB`, to model and manage financial expenses. The classes showcase object-oriented programming (OOP) concepts in Python. The `Expense` class represents an individual financial expense, while the `ExpenseDB` class manages a collection of `Expense` objects.

## Expense Class
### Attributes
- **id:** A unique identifier generated as a UUID string.
- **title:** A string representing the title of the expense.
- **amount:** A float representing the amount of the expense.
- **created_at:** A timestamp indicating when the expense was created (UTC).
- **updated_at:** A timestamp indicating the last time the expense was updated (UTC).

### Methods
1. **__init__:** Initializes the attributes.
2. **update:** Allows updating the title and/or amount, updating the updated_at timestamp.
3. **to_dict:** Returns a dictionary representation of the expense.

## ExpenseDB Class
### Attributes
- **expenses:** A list storing `Expense` instances.

### Methods
1. **__init__:** Initializes the list.
2. **add_expense:** Adds an expense.
3. **remove_expense:** Removes an expense.
4. **get_expense_by_id:** Retrieves an expense by ID.
5. **get_expense_by_title:** Retrieves expenses by title.
6. **to_dict:** Returns a list of dictionaries representing expenses.

## How to Clone the Project
To clone this project to your local machine, run the following command in your terminal:

*git clone https://github.com/Ezekiel257/altschool_first_semester_exam.git*

## How to Run the Code
Navigate to the project directory:

*cd altschool_first_semester_exam*

Ensure you have Python installed.
Run the Python script:

*python your_script_name.py*
