# Dictionaries
Countries = {"CA": "Canada",
             "US": "United States",
             "UK": "United Kingdom"}
print(Countries)
# Display the specific country
print(Countries["CA"])
# Add a new value to the dictionary
Countries["FR"] = "France"
print(Countries)
Countries["UK"] = "British Kingdom"
print(Countries)

country = input("Enter a country code: ")
for key, value in Countries.items():
    if key == country:
        print(value)
        break
    else:
        print("No country found")

print(Countries.get("UK"))

