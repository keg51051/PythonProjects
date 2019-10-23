users = {"User1": "admin",
         "User2": "asd123",
         "User3": "abc456"}

print(users)
file = open("Mydata3.txt", "w")

for k, v in users.items():
    file.write(str(k) + ': ' + str(v) + '\n')

file.close()