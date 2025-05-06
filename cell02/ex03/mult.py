#!/usr/bin/python3
num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
final = num*num2
print(final)
print(f"{num} x {num2} = {final}")
if final > 0:
    print("The result is positive.")
elif final < 0:
    print("The result is negative.")
else :
    print("The reult is positive and negative")