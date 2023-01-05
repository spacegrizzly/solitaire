# Solitaire

'Solitaire' is a board game for one player that features a board with holes and pegs or marbles that fill these holes
initially. Usually, the board is arranged in a cross-shape (English solitaire) with a centre of 3x3 and arms of 2x3.
At each position one can find one pin filling the hole, apart from the central position which remains empty.
The goal is to get rid of all the pins except for one and, ideally, have that last pin fill the central hole.

A legal move is to pick up a pin that can jump over exactly one other pin and land in a hole next to the pin it just
jumped over, so into a position either x = +/- 2 or (!) y = +/- 2. The picked up pin is placed in the hole and the
pin that it just jumped over is removed from the game.