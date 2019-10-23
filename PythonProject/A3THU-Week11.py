# Dictionaries
Countries = {"CA": "Canada",
             "US": "United States",
             "UK": "United Kingdom",
             "MX": "Mexico"}
print(Countries)

# How to delete an entry in dictionary
Countries.pop("MX")
print(Countries)
del Countries["US"]
print(Countries)

# How to remove all items in dictionary
Countries.clear()
print(Countries)