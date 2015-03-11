# Blackjack-python

A Simple simulation of a hand of blackjack. Card values are generated randomly, and deck control is not enforced. Player may hit or stand at any time. No current implementation for betting, splitting, or doubling down.

Dealer will always hit when below the minimum threshold (17), and will continue to hit while totalling less than the player until dealer wins or busts.

Regarding aces:<br>
Player may choose whether to treat an ace as 1 or 11 at time of drawing, but cannot revert an 11 to a 1 upon busting. Dealer also follows this rule, but will always select 11 if it doesn't immediately cause the dealer to bust. If the dealer's first draw is two Aces the dealer's total will be 12, since the the first Ace will automatically be an 11.
