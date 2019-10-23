Num = ['ABC'] * 5
print(Num)

temp = [34, 3.7, 21, 28.4]
print(temp[0:3:2])
print(temp[::-1])

currtemp = [-4.5, -7]
print(currtemp)

# Concatenate list
alltemp = currtemp + temp
print(alltemp)

# MUTABLE copy
# copytemp = temp
# print(copytemp)
# temp[3] = 50
# print(temp)
# print(copytemp)

# Normal copy
import copy
copytemp = copy.deepcopy(temp)
print(copytemp)
temp[3] = 50
print(temp)
print(copytemp)

