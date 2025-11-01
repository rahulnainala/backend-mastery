# -----------------------------------------
# Python OOP: Class Variables
# -----------------------------------------
# Class variables are shared across all instances.
# They are defined directly inside the class body (not inside methods).
# -----------------------------------------

class Employee:
    # Class Variables (shared by all instances)
    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        # Instance Variables (unique per object)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        # Increment class variable each time a new employee is created
        Employee.number_of_employees += 1  # <-- fixed (it was =+ before)

    def fullName(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        # Accessing class variable via instance (self.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


# -------------------------------
# Creating instances (objects)
# -------------------------------
emp1 = Employee("Rahul", "Nainala", 60000)
emp2 = Employee("Formless", "Drac", 55000)

# -------------------------------
# Printing results
# -------------------------------
print(emp1.email, "-", emp1.fullName())
print(emp2.email, "-", emp2.fullName())

print("\nTotal Employees:", Employee.number_of_employees)

# Apply raise
emp1.apply_raise()
print(f"\n{emp1.fullName()} new pay: ₹{emp1.pay}")