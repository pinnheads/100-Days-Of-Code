from os import system, name
import time

grid = {
    "7": " ",
    "8": " ",
    "9": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "1": " ",
    "2": " ",
    "3": " ",
}

turn = 1
game_on = True
no_of_turns = 0


def announcment(text):
    print("\n")
    print("-" * 80)
    print(text)
    print("-" * 80)
    print("\n")


def clear():
    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


def print_grid():
    print("\n")
    for index, item in enumerate(grid, start=1):
        if index < 7:
            print(grid[item], end=" | " if index % 3 else "\n--+---+--\n")
        else:
            print(grid[item], end=" | " if index % 3 else "\n")


def insert_symbol(symbol, index):
    grid[index] = symbol


def game(p_1, p_2):
    global turn
    if turn == 1:
        clear()
        print_grid()
        print("\n")
        location = input(
            "Player 1 where do you want to place your marker (1 - 9) "
        )
        if location == "":
            game(p_1, p_2)
        elif int(location) < 10 and int(location) > 0:
            insert_symbol(symbol=p_1, index=location)
            check_winner(p_1, p_2)
            turn = 2
        else:
            game(p_1, p_2)
    else:
        clear()
        print_grid()
        print("\n")
        location = input(
            "Player 2 where do you want to place your marker (1 - 9) "
        )
        if location == "":
            game(p_1, p_2)
        elif int(location) < 10 and int(location) > 0:
            insert_symbol(symbol=p_2, index=location)
            check_winner(p_1, p_2)
            turn = 1
        else:
            game(p_1, p_2)


def check_winner(p_1, p_2):
    global game_on, no_of_turns
    if (
        grid["7"] == grid["5"] == grid["3"] == p_1
        or grid["9"] == grid["5"] == grid["1"] == p_1
        or grid["7"] == grid["8"] == grid["9"] == p_1
        or grid["4"] == grid["5"] == grid["6"] == p_1
        or grid["1"] == grid["2"] == grid["3"] == p_1
        or grid["7"] == grid["4"] == grid["1"] == p_1
        or grid["8"] == grid["5"] == grid["2"] == p_1
        or grid["9"] == grid["6"] == grid["3"] == p_1
    ):
        clear()
        print_grid()
        announcment("Player 1 Won")
        game_on = False
    elif (
        grid["7"] == grid["5"] == grid["3"] == p_2
        or grid["9"] == grid["5"] == grid["1"] == p_2
        or grid["7"] == grid["8"] == grid["9"] == p_2
        or grid["4"] == grid["5"] == grid["6"] == p_2
        or grid["1"] == grid["2"] == grid["3"] == p_2
        or grid["7"] == grid["4"] == grid["1"] == p_2
        or grid["8"] == grid["5"] == grid["2"] == p_2
        or grid["9"] == grid["6"] == grid["3"] == p_2
    ):
        clear()
        print_grid()
        announcment("Player 2 Won")
        game_on = False
    elif no_of_turns == 8:
        clear()
        print_grid()
        announcment("Draw")
        game_on = False


def assign_players():
    player_1 = input("Player 1 choose a symbol: (X or O) ").upper()
    if player_1 == "X":
        player_2 = "O"
        print("Player 2 is 'O'")
    elif player_1 == "O":
        player_2 = "X"
        print("Player 2 is 'X'")
    else:
        print("Inavlid input! Try Again!")
        assign_players()

    return player_1, player_2


clear()
print("\nWelcome to Tic-Tac-Toe\n")
players = assign_players()
announcment("Starting Game")
time.sleep(3)

while game_on and no_of_turns < 9:
    game(players[0], players[1])
    no_of_turns += 1
