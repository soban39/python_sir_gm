# Print a string
text = "I am Sobanfarooq"
print(text)

# Define a function to add two numbers
def add(x, y):
    return x + y

# Call the function and print the result
result = add(2, 3)
print(result)

# Check types of variables in Python
x = 5
y = 6.7
print(type(x))
print(type(y))
z = True
print(type(z))

# While loop to iterate over array
arr = ["A", "B", "C"]
i = 0
while i < 3:
    i += 1
    print("hello here")

# For loop to iterate over an array
arr2 = ["sobanfarooq", "subhan"]
for i in arr2:
    print(i)

# Iterate over a tuple
tupple = ("sobanfarooq", "subhan", "Mr ghulam mustafa")
for i in tupple:
    print(i)

# Iterate over a string
strng = "sobanfarooq"
for i in strng:
    print(i)

# Iterate by index of sequences
arr3 = ["sobanfarooq", "subhan", "soban"]
for i in range(len(arr3)):
    print(arr3[i])

# Use continue and break
for letter in "geekforgeeks":
    if letter == "e":
        continue
    print("current letter:", letter)

# Program that takes age and validates if you are above 18
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible")
else:  
    print("You are not eligible")
