# -----------------------------------------
# Python OOP Basics: Classes & Instances
# -----------------------------------------
# This script demonstrates how to create a class,
# define instance variables, and use instance methods.
# -----------------------------------------

class Employee:
    """A simple Employee class to demonstrate OOP concepts."""

    # The __init__ method is called automatically when
    # a new instance of the class is created.
    # It initializes (assigns) values to the object’s attributes.
    def __init__(self, first, last, pay):
        # Instance variables (unique to each object)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # Instance method (uses 'self' to access object attributes)
    def fullName(self):
        return f"{self.first} {self.last}"

    # Another example method - calculate annual bonus
    def apply_raise(self, raise_percent):
        self.pay = int(self.pay * (1 + raise_percent))
        return self.pay


# -------------------------------
# Creating instances (objects)
# -------------------------------
emp1 = Employee('Rahul', 'Nainala', 600000)
emp2 = Employee('Formless', 'Drac', 5000000)

# -------------------------------
# Accessing instance attributes
# -------------------------------
print("****** EMAILS ********")
print(emp1.email)
print(emp2.email)
print("***********************\n")

# -------------------------------
# Calling methods
# -------------------------------
# Method 1: Calling via class name (explicitly passing instance)
print(Employee.fullName(emp1))

# Method 2: Calling via instance (Python passes 'self' automatically)
print(emp1.fullName())

# -------------------------------
# Demonstrating another instance method
# -------------------------------
print("\nBefore Raise:")
print(f"{emp1.fullName()} - Pay: ₹{emp1.pay}")

# Apply a 10% raise
emp1.apply_raise(0.10)

print("After 10% Raise:")
print(f"{emp1.fullName()} - Pay: ₹{emp1.pay}")