try:
    f = open("filename.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("FIle is closed NOW")