# Movie dictionary
movie = {"movie name": "Iron Man",
         "movie director": "Jon Favreau",
         "IMDb score": "7.9",
         "production year": "2008"}
print(movie)

# Car dictionary
car = {"brand": "Audi",
       "model": "R8",
       "year": "2018"}
print(car)

# Add and remove record in dictionary
car["color"] = "black"
car.pop("year")
car.popitem()
del car["model"]
print(car)

# Set of username_list
username_list = {"abc123", "bcd456", "qwe123", "tyu567"}
print(username_list)
# Add record to Set
username_list.add("poi987")
print(username_list)
# Remove item from Set
username_list.remove("qwe123")
username_list.discard("abc123")
username_list.pop()
print(username_list)
# Tuple of username_list
username_list = ("abc123", "bcd456", "qwe123")
print(username_list)