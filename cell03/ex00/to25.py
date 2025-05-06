#!/usr/bin/python3

num = int(input("Enter the number less than 25: "))
while num <=25:
    print("Inside the loop, my variable is " f"{num}", end = "\n")
    num = num+1
if num > 25 :
    print("Error")