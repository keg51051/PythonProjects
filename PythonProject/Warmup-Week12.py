# Cities List
citiesL = ["Toronto", "Ajax", "Ottawa", "Oshawa", "Montreal"]
print(citiesL)
# Cities Set
citiesS = {"Toronto", "Ajax", "Ottawa", "Oshawa", "Montreal"}
print(citiesS)
# Cities Tuple
citiesT = ("Toronto", "Ajax", "Ottawa", "Oshawa", "Montreal")
print(citiesT)
# Add item
citiesL.append("Vancouver")
citiesS.add("Vancouver")
print(citiesL)
print(citiesS)
# Remove item
city = input("Enter a city to remove: ")
if city in citiesL or city in citiesS:
    citiesL.remove(city)
    citiesS.remove(city)
    print(citiesL)
    print(citiesS)
else:
    print("City not found")
