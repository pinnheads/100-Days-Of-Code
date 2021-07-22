# Challenge 1
# Write a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.

# e.g. 86 is even because 86 ÷ 2 = 43

# 43 does not have any decimal places. Therefore the division is clean.

# e.g. 59 is odd because 59 ÷ 2 = 29.5

# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# e.g.

# 6 ÷ 2 = 3 with no remainder.

# 6 % 2 = 0

# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.

# 5 % 2 = 1

# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.

# 14 % 4 = 2

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input 1

# 43

# Example Output 1

# This is an odd number.

# Example Input 2

# 94

# Example Output 2

# This is an even number.
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")

####################################################################################
# BMI Calculator 2.0
# Instructions

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.

# https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
# Example Input

# weight = 85

# height = 1.75

# Example Output

# 85 ÷ (1.75 x 1.75) = 27.755102040816325

# Your BMI is 28, you are slightly overweight.
print('Welcome to my bmi calculator')

bmi=(float(input('How much do you weigh? ')))/(float(input("How tall are you in m? ")))**2

if round(bmi,2)<18.5:
    print(f'Your BMI is {bmi}You are underweight')

elif round(bmi,2)>=18.5 and round(bmi,2)<=24.5:
    print(f"Your BMI is {bmi}, You weigh normal")

else:
    print(f"Your BMI is {bmi}, You are overweight")

########################################################################################
# Challenge 3
# Leap Year
# 💪This is a Difficult Challenge 💪
# Instructions

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.

#     on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)

# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)

# 2100 ÷ 100 = 21 (Not Leap)

# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input 1

# 2400

# Example Output 1

# Leap year.

# Example Input 2

# 1989

# Example Output 2

# Not leap year.
print("Welcome to the Leap Year Test")

year = int(input("Enter the year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a Leap year")
        else:
            print(f"The year {year} is not a Leap year")
    else:
        print(f"The year {year} is a Leap year")
else:
    print(f"The year {year} is a Leap year")

####################################################################################
# Challenge 3
# Love Calculator
# 💪 This is a Difficult Challenge 💪
# Instructions

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

#     Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

# e.g.

# name1 = "Angela Yu"

# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."
# Example Input 1

# name1 = "Kanye West"

# name2 = "Kim Kardashian"

# Example Output 1

# Your score is 42, you are alright together.

# Example Input 2

# name1 = "Brad Pitt"

# name2 = "Jennifer Aniston"

# Example Output 2

# Your score is 73.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_1 = name1.lower()
lower_2 = name2.lower()

count_true = lower_1.count("t") + lower_1.count("r") + lower_1.count("u") + lower_1.count("e") + lower_2.count("t") + lower_2.count("r") + lower_2.count("u") + lower_2.count("e")

count_love = lower_1.count("l") + lower_1.count("o") + lower_1.count("v") + lower_1.count("e") + lower_2.count("l") + lower_2.count("o") + lower_2.count("v") + lower_2.count("e")

score_str = str(count_true) + str(count_love)

score = int(score_str)

if score < 10 or score > 90: 
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50: 
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")
