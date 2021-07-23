# Randomisation
import random

random_int = random.randint(1, 10) #gives a random integer between the given range
print(random_int)

random_float = random.random() # random floating numbers between 0.9999999 - 0.9999999
print(random_float)

random_float * 5 # random floating numbers between 0.9999999 - 4.9999999

# Lists
# A data structure, widely used.
fruits = ["Apple", "Pear", "Mango"]

# index starts with 0
print(fruits[0])

# -1 will point to the last item
print(fruits[-1])

# Reassign items
fruits[1] = "Orange"

# Add items in the end
fruits.append("Banana")

# nested lists
vegetables = ["Spinach", "Tomatoes", "Celery", "Potatoes"]

new_list = [fruits, vegetables]
