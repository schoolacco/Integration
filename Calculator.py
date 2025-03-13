from math_operations import Addition
print("Insert you numbers to be added")
num1 = input("Number 1: ")
num2 = input("Number 2: ")
Result = Addition.add_numbers(num1, num2)
if Result != "One or more value(s) were not an integer":
  print(f"The sum of {num1} and {num2} is {Result}")
else:
  print(Result)