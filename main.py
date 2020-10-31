# dictionary and list.

player_dict = {}
sorted_list_keys = []

# Define the function sortdictkeys()

def sortdictkeys():
    sorted_list_keys = sorted(player_dict.keys())
    return sorted_list_keys

# Define the function outputroster().

def outputroster():
    sorted_list_keys = sortdictkeys()
    print("ROSTER")


    for i in sorted_list_keys:
        # Display jersey number and player's rating
        print("Jersey number: " + str(i) + ", Rating: " + str(player_dict[i]))

# Define the function addPlayer().

def addplayer():
    # Prompt to enter a jersey number.
    print("Enter a new player's jersey number:")
    jersey_num = int(input())

 # Make sure the Jersey number entered is valid and if not enter other jersey number.

    while (jersey_num < 0) or (jersey_num > 99):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter a new player's jersey number:")
        jersey_num = int(input())

# User to enter player's rating.
    print("Enter the player's rating:")
    player_rating = int(input())

# Make sure the Jersey number entered is valid and if not enter other jersey

    while (player_rating < 1) or (player_rating > 9):
        print("Invalid Rating! Please enter again!")
        print("Enter the player's rating:")
        player_rating = int(input())

# Update the dictionary with new entry.
    player_dict.update({jersey_num: player_rating})

# Define the function removeplayer

def removeplayer():
    # User to enter a jersey number.

    print("Enter a jersey number:")
    jersey_num = int(input())

# Make sure the Jersey number entered is valid and if not enter other jersey

    while (jersey_num < 0) or (jersey_num > 99):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter a jersey number:")
        jersey_num  = int(input())

        while (jersey_num < 0) or (jersey_num > 99):
            print("Invalid Jersey Number! Please " + "enter again!")
            print("Enter a jersey number:")
            jersey_num = int(input())

        if jersey_num in player_dict.keys():
            del player_dict[jersey_num]

# Define the function updateplayer

def updatePlayer():
    # Prompt the user to enter a jersey number.
    print("Enter a jersey number:")
    jersey_num = int(input())
# Jersey number enter greater than 0 but less than 99
    while (jersey_num < 0) or (jersey_num > 99):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter a jersey number:")
        jersey_num = int(input())

    print("Enter a new rating for player:")
    player_rating = int(input())

    while (player_rating < 1) or (player_rating > 9):
        print("Invalid Rating! Please enter again!")
        print("Enter a new rating for player:")
        player_rating = int(input())

    # Update
    player_dict[jersey_num] = player_rating

# Define the function outputPlayerAboveRating().

def outputplayeraboverating():
    # Prompt the user to enter a rating.
    print("Enter a rating:")
    rating = int(input())


    while (player_rating < 1) or (player_rating > 9):
        print("Invalid Rating! Please enter again!")
        print("Enter a rating:")
        rating = int(input())
    print("ABOVE 4")

    sorted_list_keys = sortdictkeys()
    # Traverse the list of keys.

    for i in sorted_list_keys:
        if player_dict[i] > rating:
            # Display the current player's jersey number and rating.
            print("Jersey number: " + str(i) + ", Rating: " + str(player_dict[i]))

# Start a for loop from 1 to 6.

for i in range(1, 6):

    # Prompt the user to enter player's jersey number.
    print("Enter player " + str(i) + "'s jersey number:")
    jersey_num = int(input())


    while (jersey_num < 0) or (jersey_num > 99):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter player " + str(i) + "'s jersey number:")
        jersey_num = int(input())

    # Prompt the user to enter a player's rating.
    print("Enter player " + str(i) + "'s rating:")
    player_rating = int(input())


    while (player_rating < 1) or (player_rating > 9):
        print("Invalid Rating! Please enter again!")
        print("Enter player " + str(i) + "'s rating:")
        player_rating = int(input())
    print()
    player_dict[jersey_num] = player_rating

outputroster()
print()

# Start a while loop.

while True:
    # Display menu of choices.
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()

    # Prompt the user to enter a choice.
    print('Choose an option:')
    user_choice = input()

    # If the user's choice is a, then call the function addplayer
    if user_choice == 'a':
        addplayer()


    # If the user's choice is d, then call the function removeplayer().
    elif user_choice == 'd':
        removeplayer()

    # If the user's choice is u, then call the function updateplayer().
    elif user_choice == 'u':
        updatePlayer()

    # If the user's choice is r, then call the functionmoutputplayeraboverating().
    elif user_choice == 'r':
        outputplayeraboverating()

    # If the user's choice is o, then call the function outputroster().
    elif user_choice == 'o':
        outputroster()

    # If the user's choice is q, then break the loop.
    elif user_choice == 'q':
        break
    print()
