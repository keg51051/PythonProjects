users = {"User1": "admin",
         "User2": "asd123",
         "User3": "abc456"}

print(users)
file = open("Mydata3.txt", "w")

file.write('\n'.join(users))

file.close()