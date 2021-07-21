# Challenge 1
# Instructions

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.
# Example Input

# 39

# Example Output

# 3 + 9 = 12

# 12
two_digit_number = input("Type a two digit number: ")
sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum)

######################################################################################

# Challenge 2
# BMI Calculator
# Instructions

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# Warning you should convert the result to a whole number.
# Example Input

# weight = 80

# height = 1.75

# Example Output

# 80 ÷ (1.75 x 1.75) = 26.122448979591837

# 26
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = round(int(weight) / (float(height)**2))
print(BMI)

######################################################################################

# Challenge 2
# Your Life in Weeks
# Instructions

# I was reading this article by Tim Urban - Your Life in Weeks and realised just 
# how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

#     You have x days, y weeks, and z months left. 

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input

# 56

# Example Output

# You have 12410 days, 1768 weeks, and 408 months left.
age = input("What is your current age?")
remaining_years = 90 - int(age)
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
