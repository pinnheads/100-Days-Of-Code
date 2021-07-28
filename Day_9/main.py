# Dictionaries
# key - value pairs -> {key: value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Add new items
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# Edit a value
programming_dictionary["Bug"] = "A moth in your Computer"
print(programming_dictionary["Bug"])

# For loop with dictionary
for key in programming_dictionary:
    print(key) # <- prints key
    print(programming_dictionary[key]) # <- prints value for the key

# Nesting lists and dictionary in dictionaries
# Dict1 = {
#   key1: [list1]
#   key2: {dict2}
# }

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

travel_log = [
{
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12,
},
{
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
},
]


# Wipe a dictionary
programming_dictionary = {}
