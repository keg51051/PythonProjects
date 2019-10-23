citiesL = ["Toronto", "Ajax", "Ottawa", "Oshawa", "Montreal"]

file = open("Mydata2.txt", "w")

file.write('\n'.join(citiesL))

file.close()