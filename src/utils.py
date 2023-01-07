import pyfiglet


# takes a player as a parameter and prints their hand and score on one line
def print_player(player):
    hand_string = ""
    for card in player.hand:
        hand_string += str(card.name) + ", "
    print(pyfiglet.figlet_format(hand_string + "Score: " + str(player.score)))


# display blackjack logo
# def print_logo():
#     print(pyfiglet.figlet_format("Blackjack", font=))

# use font "slant" for the logo
