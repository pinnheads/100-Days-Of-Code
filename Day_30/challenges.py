# Challenge 1
# IndexError Handling
# Issue

# We've got some buggy code. Try running the code. The code will crash and give 
# you an IndexError. This is because we're looking through the list of fruits 
# for an index that is out of range.
# Bad Output

# https: // cdn.fs.teachablecdn.com/GNPYLwHXQFOUTylnvWvK
# Instructions

# Use what you've learnt about exception handling to prevent the program from 
# crashing. If the user enters something that is out of range just print a 
# default output of "Fruit pie". e.g.

# https: // cdn.fs.teachablecdn.com/6sNP0lqETeG99crht28k
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(4)
except IndexError:
    print("Fruit pie")
###############################################################################
# Challenge 2
# KeyError Handling
# Issue

# We've got some buggy code, try running the code. The code will crash and give 
# you a KeyError. This is because some of the posts in the facebook_posts don't 
# have any "Likes".
# Bad Output

# https: // cdn.fs.teachablecdn.com/u1humLqATmXKtN2Uec9A
# Instructions

# Use what you've learnt about exception handling to prevent the program from 
# crashing.
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        print(f"{post} - This post didn't have any likes")


print(total_likes)
