try:
    num1 = 7
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print("An error occurred")
    print("Due to zero division")
finally:
    print("This code will run no matter what")
