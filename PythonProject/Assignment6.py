try:
    with open("dataFile.txt", "r") as f:
        for users in f:
            user = users.split(",")
            print("First Name: ", user[0])
            print("Last Name: ", user[1])
            print("Email: ", user[2])
except FileNotFoundError as arg:
    print("File not found", arg)
finally:
    f.close()

