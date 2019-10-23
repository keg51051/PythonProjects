# Dictionaries
Countries = {"CA": "Canada",
             "US": "United States",
             "UK": "United Kingdom",
             "MX": "Mexico"}

# Prompt user to enter a country code
# if the country_code is exist
# remove it, otherwise display error
key = input("Enter a country code: ")
if Countries.get(key):
    Countries.pop(key)
else:
    print("Country not found to remove")
print(Countries)

# country = input("Enter a country code: ")
# for key, value in Countries.items():
#     if key == country:
#         Countries.pop(key)
#         print(value + " is removed")
#         print(Countries)
#         break
#     else:
#         print("Country not found to remove")
