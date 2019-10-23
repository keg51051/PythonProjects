try:
    with open("Mydata100.txt") as f:
        print(f.read())
except:
    print("File operation ERROR")