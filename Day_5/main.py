# For Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# Range Function
for number in range(1, 101):
    print(number)

# Steps in range
total = 0
for number in range(1, 101, 2):
    total += number
print(total)

# If - Else statements in For Loops
for number in range(1, 101):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	elif number % 5 == 0:
		print("Buzz")
	elif number % 3 == 0:
		print("Fizz")
	else:
		print(number)