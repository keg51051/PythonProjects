file = open("Mydata2.txt", "r")

city = []

data = file.readline()
while(data):
    city.append(data.strip())
    data = file.readline()
print(city)

# for i in file:
#     city.append(i.strip())
# print(city)

# content = file.read()
# print(content)
# city = content.split("\n")
# print(city)

file.close()