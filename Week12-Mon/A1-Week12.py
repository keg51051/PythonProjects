# Open file
file = open("Mydata1.txt", "r")

# Read file
content = file.read()
# Display file data
print(content)

another = file.read()
print(another)

# Close file
file.close()
