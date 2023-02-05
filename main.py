# random for dealing card and choosing suit
import random

def main():
    # variables
    playerTokens = 500

    # only show instructions once player has opened
    # the game
    instructions()

    # loop game
    while True:
        # loop until a valid bet has been entered
        while True:
            print("\nYou currently have:", playerTokens, "tokens.")

            # get player's bet
            # try except used to make sure valid int is input
            try:
                bet = int(input("Enter your bet: "))

                # validate bet
                if bet > playerTokens:
                    print("Error! Please enter a valid bet!")
                elif bet < 1:
                    print("Error! Please enter a valid bet!")
                else:
                    # break if valid
                    break

            except:
                print("Error! Please enter a valid bet!")

        # deal player
        input("\nPress enter to deal your cards: ")

        playerPoints1 = deal()
        playerPoints2 = deal()

        # check for black jack
        isBlackJack = blackJack(playerPoints1, playerPoints2)

        if isBlackJack:
            playerPoints = 21
        else:
            playerPoints = playerPoints1 + playerPoints2

        print("\nYour current points: ", playerPoints)

        # deal dealer
        input("\nPress enter to deal dealer's card: ")

        dealerPoints1 = deal()

        print("\nDealer's current points: ", dealerPoints1)

        # hit or stand
        option = ""

        # hit as long as player hasn't chose stand or is bust
        while option != "stand" and playerPoints < 21:

            option = hitOrStand()

            # hit
            if option == "hit":
                playerPoints += deal()

                print("\nYour current points: ", playerPoints)

            # end if 21 or bust
            if playerPoints == 21:
                print("Automatic stand on 21.")

                option = "stand"
            elif playerPoints > 21:
                print("Bust!")

        # deal dealer's next cards
        input("\nPress enter to deal dealer's card: ")

        dealerPoints2 = deal()

        # check for black jack
        isBlackJack = blackJack(dealerPoints1, dealerPoints2)

        if isBlackJack:
            dealerPoints = 21
        else:
            dealerPoints = dealerPoints1 + dealerPoints2

        print("\nDealer's current points: ", dealerPoints)

        # dealer stands on 17 and more
        while dealerPoints < 17:
            input("\nPress enter to deal dealer's card: ")

            dealerPoints += deal()

            print("\nDealer's current points: ", dealerPoints)

        # win or lose
        # dealer bust
        if playerPoints > 21:
            print("\nPlayer bust! You lose!")

            # take player's bet
            playerTokens -= bet
        elif dealerPoints > 21:
            print("\nDealer bust! You win!")

            # give player their tokens
            playerTokens += bet
        elif playerPoints == dealerPoints:
            print("\nPush! You draw!")
        elif playerPoints < dealerPoints:
            print("\nYou lose!")

            # take player's bet
            playerTokens -= bet
        elif playerPoints > dealerPoints:
            print("\nYou win!")

            # give player their tokens
            playerTokens += bet

        # current tokens
        print("\nYou currently have", playerTokens, "tokens.")

        # end with 0 tokens
        if playerTokens <= 0:
            print("\nAll out of tokens!")
            print("Thanks for playing!")

            break

        # ask player to continue
        playAgain = input("\nEnter 'y' to play again or any key to exit: ")

        if playAgain.lower() != "y":
            print("\nThanks for playing!")

            break


# function for showing instructions/rules
def instructions():
    print("Welcome!")

    input("Press enter to continue: ")


# function for dealing cards and getting points
def deal():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # randomly choose from the list
    points = cards[random.randint(0, 12)]

    # find name of card based on points
    card = cardName(points)

    print("\n" + card, points)

    return points


# function for getting cards name
def cardName(points):
    # pick the card type
    if points == 1:
        type = "Ace "
    elif points == 2:
        type = "Two "
    elif points == 3:
        type = "Three "
    elif points == 4:
        type = "Four "
    elif points == 5:
        type = "Five "
    elif points == 6:
        type = "Six "
    elif points == 7:
        type = "Seven "
    elif points == 8:
        type = "Eight "
    elif points == 9:
        type = "Nine "
    else:
        # randomly choose type for 10
        randomType = random.randint(0, 3)

        if randomType == 0:
            type = "Ten "
        elif randomType == 1:
            type = "Jack "
        elif randomType == 2:
            type = "Queen "
        else:
            type = "King "

    # randomly pick suit
    randomSuit = random.randint(0, 3)

    if randomSuit == 0:
        suit = "of clubs"
    elif randomSuit == 1:
        suit = "of diamonds"
    elif randomSuit == 2:
        suit = "of hearts"
    else:
        suit = "of spades"

    # add them together
    card = type + suit

    return card


# function to check for black jack
def blackJack(points1, points2):
    # check for black jack
    if points1 == 1:
        if points2 == 10:
            print("\nBlack Jack!")

            # set isBlackJack to true
            return True
    elif points2 == 1:
        if points1 == 10:
            print("\nBlack Jack!")

            # set isBlackJack to true
            return True
    else:
        # set isBlackJack to false
        return False


# function for asking hit or stand
def hitOrStand():
    option = ""

    while option != "hit" and option != "stand":
        option = input("\nEnter 'Hit' 'Stand': ")

        option = option.lower()

        if option != "hit" and option != "stand":
            print("Error! please enter a valid option!")

    return option


main()

