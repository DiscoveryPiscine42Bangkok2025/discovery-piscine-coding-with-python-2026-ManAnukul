#!/usr/bin/env python3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a * b

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

print("Result:", result)
