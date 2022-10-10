# printing odd / even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# printing positive or negative.
n2 = int(input("Enter a number: "))
if n2 > 0:
    print("The number is positive")
elif n2 < 0:
    print("The number is negative")
else:
    print("Zero")

# To display last digit of number.
n1 = int(input("Enter any number: "))
n2 = (n1 % 10)
print(n2)

# last digit of number is divisible by 7 or not.
n0 = int(input("Enter any number: "))
n = n0 % 10
if (n % 7 == 0):
    print("Divisible by 7")
else:
    print("Not divisible by 7")

# leap year  or not.
num1 = int(input("Enter any number: "))
if num1 % 4 == 0:
    print("Leap Year")
else:
    print("Not a leap year")

# days of the week.
day = int(input("Enter any value (1-7)"))
if (day == 1):
    print("Sunday")
if (day == 2):
    print("Monday")
if (day == 3):
    print("Tuesday")
if (day == 4):
    print("Wednesday")
if (day == 5):
    print("Thursday")
if (day == 6):
    print("Friday")
if (day == 7):
    print("Saturday")
elif (day >7 or day <0):
    print("Invalid")
