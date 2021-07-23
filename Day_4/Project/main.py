import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
choices_name = ["Rock", "Paper", "Scissors"]

player_choice = int(input("Choose one:\n1. Rock\n2. Paper\n3. Scissors\n")) - 1
if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose!")
 
print("\nPlayer Chose:\n")
print(choices_name[player_choice])
print(choices[player_choice])

computer_choice = random.randint(0,2)
print("Computer Chose:\n")
print(choices_name[computer_choice])
print(choices[computer_choice])

if player_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and player_choice == 2:
  print("You lose")
elif computer_choice > player_choice:
  print("You lose")
elif player_choice > computer_choice:
  print("You win!")
elif computer_choice == player_choice:
  print("It's a draw")