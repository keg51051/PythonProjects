try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("An error occurred")
    print("Due to zero division")
finally:
    print("This code will run no matter what")