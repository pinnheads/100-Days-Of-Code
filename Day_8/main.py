# Functions with Arguments/Parameters
def my_function(number): # <- Parameter
    result = number + 2
    return result

print(my_function(10)) # <- Argument


# Positional Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack Bauer", "Nowhere") # Prints -> Hello Jack Bauer \n What is it like in Nowhere?

greet_with("Nowhere", "Jack Bauer") # Prints -> Hello Nowhere \n What is it like in Jack Bauer?

# Keyword  Arguments
greet_with(name = "Jack Bauer", location = "Nowhere") # Prints -> Hello Jack Bauer \n What is it like in Nowhere?

greet_with(location = "Nowhere", name = "Jack Bauer") # Prints -> Hello Jack Bauer \n What is it like in Nowhere?