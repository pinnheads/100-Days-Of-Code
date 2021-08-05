# Creating Classes
class User:
    # Constructor functions gets called with every new instance of the class
    def __init__(self, user_id, username): 
        # self is the object being created itself and helps in assigning values to variables
        print("New user being created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Jack")
user_2 = User("002", "Matt")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
