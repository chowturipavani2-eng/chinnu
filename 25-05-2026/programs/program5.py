a = input("enter the first variable value (a):")
b = input("enter the second variable value (b):")
print(f"original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"swapped values: a = {a},b = {b}")
