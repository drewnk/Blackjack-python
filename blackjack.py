# Drew Nagy-Kato
# Blackjack

# Simple simulation of a hand of blackjack. Card values are generated randomly,
# and deck control is not enforced. Player may hit or stand at any time. No
# current implementation for betting, splitting, or doubling down.

# Dealer will always hit when below the minimum threshold (17), and will
# continue to hit while totalling less than the player until dealer wins or
# busts.

# Aces:
# Player may choose whether to treat an ace as 1 or 11 at time of drawing, but
# cannot revert an 11 to a 1 upon busting. Dealer also follows this rule, but
# will always select 11 if it doesn't immediately cause the dealer to bust. If
# the dealer's first draw is two Aces the dealer's total will be 12, since the
# the first Ace will automatically be an 11.

import random

BLACKJACK = 21
ACE = 11
DEALER_MIN = 17

def main():

    random.seed()

    total = firstDraw()

    if total == BLACKJACK:
        print "A natural blackjack! You win!"
        return
    
    while total < BLACKJACK:
        if total >= BLACKJACK:
            break
        else:
            choice = int(input("Do you want it hit (1) or stay (2)?\n"))
            
            if choice == 2:
                print "You decide to stay at: %d\n" % total
                break
            else:
                newCard = drawCard(total)
                total = total + newCard
                print "Your total is %d." % total

    if total > BLACKJACK:
        print "You bust!"
    else:
        dealer = playDealer(total)
        
        if dealer >= total and dealer <= BLACKJACK:
            print "The dealer wins!"
        elif dealer > BLACKJACK:
            print "The dealer busts. You win!"
        else:
            print "You win!"
    

# player's initial hand
def firstDraw():
    
    faceUp = drawCard(0)
    faceDown = drawCard(faceUp)

    total = faceUp + faceDown

    print "Your total is %d.\n" % total

    return total

# player draws a card
def drawCard(total):

    newCard = random.randint(2, 11)

    if newCard == ACE and total + newCard <= BLACKJACK:
            newCard = int(input("You drew an Ace. Is it a 1 or 11?\n"))
    elif newCard == ACE:
        print "You drew an Ace, but it must automatically be a 1."
        newCard = 1
    else:
        print "You drew a %d." % newCard

    return newCard


# simulates the dealer drawing a card
def drawDealer(total):

    newCard = random.randint(2, 11)

    if newCard == ACE and total + newCard <= BLACKJACK:
        print "The dealer drew an Ace. It is an 11."
    elif newCard == ACE:
        print "The dealer drew an Ace, but it must automatically be a 1."
        newCard = 1
    else:
        print "The dealer drew a %d." % newCard

    return newCard


# simulates dealer play
def playDealer(player):
    
    dealer = drawDealer(drawDealer(0))
    print "The dealer's total is %d.\n" % dealer
    
    while dealer < DEALER_MIN:
        dealer = dealer + drawDealer(dealer)
        print "The dealer's total is %d.\n" % dealer

    if dealer >= player:
        return dealer
    else:
        while dealer < player:
            dealer = dealer + drawDealer(dealer)
            print "The dealer's total is %d.\n" % dealer 

        return dealer

main()
