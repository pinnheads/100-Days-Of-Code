# Challenge 1
# List Comprehension 1
# Instructions

# You are going to write a List Comprehension to create a new list called 
# squared_numbers. This new list should contain every number in the list numbers
# but each number should be squared.

# e.g. `4 * 4 = 16`

# 4 squared equals 16.

# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
# Example Output

# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [ n ** 2 for n in numbers]
print(squared_numbers)

################################################################################
# Challenge 2
# List Comprehension 2
# Instructions

# You are going to write a List Comprehension to create a new list called result
# . This new list should only contain the even numbers from the list numbers.

# DO NOT modify the List numbers directly. Try to use List Comprehension instead
# of a Loop.
# Example Output

# [2, 8, 34]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

################################################################################
#Challenge 3
# List Comprehension 3

# 💪 This exercise is HARD
# Instructions

# Take a look inside file1.txt and file2.txt. They each contain a bunch of 
# numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that 
# are common in both files.

# e.g. if file1.txt contained:

# 1

# 2

# 3

# and file2.txt contained:

# 2

# 3

# 4

# result = [2, 3]

# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
# Example Output

# [3, 6, 5, 33, 12, 7, 42, 13]

def format_numbers(list_num):
    print(f"Got - {list_num}")
    formatted_nums = []
    for num in list_num:        
        formatted_nums.append(int(num.strip("\n")))
    print(f"Returned - {formatted_nums}")
    return formatted_nums

with open("file1.txt") as file1:
    file1_numbers = file1.readlines()
    f1_nums = format_numbers(file1_numbers)
with open("file2.txt") as file2:
    file2_numbers = file2.readlines()
    f2_nums = format_numbers(file2_numbers)

common_numbers = [n for n in f1_nums if n in f2_nums]
print(common_numbers)

###############################################################################
# Challenge 4
# Dictionary Comprehension 1
# Instructions

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

# Try Googling to find out how to convert a sentence into a list of words.

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Example Output

# {

#     'What': 4,

#     'is': 2,

#     'the': 3,

#     'Airspeed': 8,

#     'Velocity': 8,

#     'of': 2,

#     'an': 2,

#     'Unladen': 7,

#     'Swallow?': 8

# }
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(" ")
result = {word:len(word) for word in words}
print(result)
###############################################################################
# Challenge 5
# Dictionary Comprehension 2
# Instructions

# You are going to use Dictionary Comprehension to create a dictionary called 
# weather_f that takes each temperature in degrees Celsius and converts it into 
# degrees Fahrenheit.

# To convert temp_c into temp_f:

# (temp_c * 9/5) + 32 = temp_f

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension 
# instead of a Loop.
# Example Output

# {

#     'Monday': 53.6,

#     'Tuesday': 57.2,

#     'Wednesday': 59.0,

#     'Thursday': 57.2,

#     'Friday': 69.8,

#     'Saturday': 71.6,

#     'Sunday': 75.2

# }
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
def c_to_f(c_temp):
    return (c_temp * 9/5) + 32
weather_f = { day:c_to_f(temp_c) for (day, temp_c) in weather_c.items()}
print(weather_f)
