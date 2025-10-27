age = float(input("Hi there! Please enter your age:"))
counter = 0
for i in range(1, int(age) + 1):
    counter += i
print(f"The sum of all numbers from 1 to {int(age)} is: {counter}.")