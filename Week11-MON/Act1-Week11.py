#Create a list
course=['CPAN204', 'CPAN205','CPAN203','CPAN202','CPAN201']

print ("List of all items")
print (course)

#display items 2,3,4
print (course[2:5])
#everything after 3rd item
print (course[3:])
#everything before 3rd item
print (course[:3])
#list in sorted order
course.sort()
print(course)
#list in descending sorted order
course.reverse()
course.sort(reverse=True)
print(course)
