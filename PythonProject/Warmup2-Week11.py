num1= input("Enter first number ")
num2 = input("Enter second number ")
num3 = input("Enter third number ")

numbers = [num1, num2, num3]

print("The maximum number is:", max(map(int, numbers)))
print("The minimum number is:", min(map(int, numbers)))
print("The number of numbers entered is:", len(numbers))