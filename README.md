# Task_5-data_structure

## Overview
This contains two console applications:
1. Assignment To-Do List Manager  
2. Expense Tracker System  

Both programs are designed to practice core Python concepts such as loops, conditionals, input handling, lists, nested lists, tuples, list comprehensions, and basic data validation.

---

## 1. Assignment To-Do List Manager

### Features
- Stores assignments using a nested list structure `[subject, status]`
- Add new subjects to the list
- Remove existing subjects
- Update assignment status (complete/incomplete)
- Displays all assignments with current status
- Uses indexing and list methods

### How it works
- User views a preloaded list of subjects
- User can add or remove subjects from the list
- Each subject has a completion status
- User can update the status of any subject
- Updated assignment list is displayed after changes



## 2. Expense Tracker System

### Features
- Add expenses with:
  - Category
  - Amount
- Input validation for numeric amounts
- Stores expenses as tuples `(category, amount)`
- View expenses by:
  - Category filter (using list comprehension)
  - Minimum amount filter
  - Full expense list
- Handles empty expense list cases

### How it works
- User selects "add" to store expenses
- User can view expenses in different formats
- Expenses are filtered using list comprehensions
- Program continues until user chooses to exit



## Concepts Used
- Loops (while and for)
- Conditional statements
- Lists and nested lists
- Tuples (immutable data structures)
- List comprehensions
- Input validation and type conversion
- Program flow control


## Tools Used
- Python
- Visual Studio Code
