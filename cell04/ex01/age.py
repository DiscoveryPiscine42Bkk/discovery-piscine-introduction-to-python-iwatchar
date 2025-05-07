#!/usr/bin/python3

b = int(input("Please tell your age : "))
print(f"You are currently {b} years old.")

a = 10
while a <= 30:
    print(f"In {a} years, you'll be {a+b} years old.", end ="\n")
    a += 10