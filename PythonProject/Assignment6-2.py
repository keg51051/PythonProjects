try:
    first = input("Enter first name to search: ")
    if not first.strip():
        print("You should enter something.")
    else:
        print("You entered", first, "\n")
        with open("dataFile.txt", "r") as f:
            for users in f:
                user = users.split(",")
                if user[0] == first:
                    print("First Name: ", user[0])
                    print("Last Name: ", user[1])
                    print("Email: ", user[2])

        f.close()

except FileNotFoundError as arg:
    print("File not found", arg)

