# Solitaire

'Solitaire' is a board game for one player that features a board with holes and pegs or marbles that fill these holes
initially. Usually, the board is arranged in a cross-shape (English solitaire) with a centre of 3x3 and arms of 2x3.
At each position one can find one pin filling the hole, apart from the central position which remains empty.
The goal is to get rid of all the pins except for one and, ideally, have that last pin fill the central hole.

A legal move is to pick up a pin that can jump over exactly one other pin and land in a hole next to the pin it just
jumped over, so into a position either x = +/- 2 or (!) y = +/- 2. The picked up pin is placed in the hole and the
pin that it just jumped over is removed from the game.


# Results obtained so far

Solution with one pin found!
Move list        [[(3, 1), (3, 3)], [(1, 2), (3, 2)], [(2, 4), (2, 2)], [(2, 6), (2, 4)], [(0, 3), (2, 3)], [(3, 2), (1, 2)], [(2, 3), (2, 5)], [(0, 4), (2, 4)], [(3, 4), (1, 4)], [(0, 2), (2, 2)], [(4, 6), (2, 6)], [(4, 4), (4, 6)], [(6, 4), (4, 4)], [(4, 3), (4, 5)], [(2, 1), (2, 3)], [(5, 2), (3, 2)], [(4, 0), (4, 2)], [(6, 2), (6, 4)], [(2, 3), (4, 3)], [(4, 3), (4, 1)], [(2, 6), (2, 4)], [(2, 0), (4, 0)], [(4, 6), (4, 4)], [(1, 4), (3, 4)], [(3, 4), (5, 4)], [(4, 0), (4, 2)], [(6, 4), (4, 4)], [(3, 2), (5, 2)], [(5, 2), (5, 4)], [(5, 4), (3, 4)], [(3, 4), (3, 6)]]
Pins in  1.0
     0    1  2  3  4    5    6
0  NaN  NaN  0  0  0  NaN  NaN
1  NaN  NaN  0  0  0  NaN  NaN
2  0.0  0.0  0  0  0  0.0  0.0
3  0.0  0.0  0  0  0  0.0  0.0
4  0.0  0.0  0  0  0  0.0  0.0
5  NaN  NaN  0  0  0  NaN  NaN
6  NaN  NaN  0  1  0  NaN  NaN


Solution with one pin found!
Move list        [[(5, 3), (3, 3)], [(4, 1), (4, 3)], [(6, 2), (4, 2)], [(4, 3), (4, 1)], [(6, 4), (6, 2)], [(4, 0), (4, 2)], [(2, 0), (4, 0)], [(2, 1), (4, 1)], [(3, 2), (5, 2)], [(4, 5), (4, 3)], [(4, 0), (4, 2)], [(2, 4), (4, 4)], [(5, 4), (3, 4)], [(2, 3), (2, 1)], [(2, 5), (4, 5)], [(4, 3), (4, 1)], [(0, 3), (2, 3)], [(3, 3), (1, 3)], [(0, 2), (2, 2)], [(6, 2), (4, 2)], [(0, 4), (2, 4)], [(4, 1), (4, 3)], [(2, 1), (2, 3)], [(2, 3), (2, 5)], [(4, 6), (4, 4)], [(4, 3), (4, 5)], [(2, 6), (4, 6)], [(4, 6), (4, 4)], [(4, 4), (2, 4)], [(2, 5), (2, 3)], [(1, 3), (3, 3)]]
Pins in  1.0
     0    1  2  3  4    5    6
0  NaN  NaN  0  0  0  NaN  NaN
1  NaN  NaN  0  0  0  NaN  NaN
2  0.0  0.0  0  0  0  0.0  0.0
3  0.0  0.0  0  1  0  0.0  0.0
4  0.0  0.0  0  0  0  0.0  0.0
5  NaN  NaN  0  0  0  NaN  NaN
6  NaN  NaN  0  0  0  NaN  NaN

Solution with one pin found!
Move list        [[(3, 1), (3, 3)], [(3, 4), (3, 2)], [(5, 4), (3, 4)], [(5, 3), (3, 3)], [(4, 6), (4, 4)], [(4, 1), (4, 3)], [(2, 5), (4, 5)], [(3, 3), (3, 1)], [(6, 2), (4, 2)], [(2, 6), (4, 6)], [(4, 3), (4, 1)], [(4, 0), (4, 2)], [(2, 3), (2, 5)], [(0, 4), (2, 4)], [(1, 2), (3, 2)], [(3, 2), (5, 2)], [(3, 4), (5, 4)], [(4, 6), (4, 4)], [(5, 4), (3, 4)], [(0, 2), (0, 4)], [(2, 0), (2, 2)], [(3, 4), (1, 4)], [(0, 4), (2, 4)], [(2, 5), (2, 3)], [(2, 3), (2, 1)], [(6, 4), (6, 2)], [(3, 0), (3, 2)], [(6, 2), (4, 2)], [(4, 2), (2, 2)], [(2, 1), (2, 3)], [(1, 3), (3, 3)]]
Pins in  1.0
     0    1  2  3  4    5    6
0  NaN  NaN  0  0  0  NaN  NaN
1  NaN  NaN  0  0  0  NaN  NaN
2  0.0  0.0  0  0  0  0.0  0.0
3  0.0  0.0  0  1  0  0.0  0.0
4  0.0  0.0  0  0  0  0.0  0.0
5  NaN  NaN  0  0  0  NaN  NaN
6  NaN  NaN  0  0  0  NaN  NaN

Solution with one pin found!
Move list        [[(3, 1), (3, 3)], [(1, 2), (3, 2)], [(2, 4), (2, 2)], [(0, 3), (2, 3)], [(0, 4), (2, 4)], [(3, 3), (3, 1)], [(3, 4), (1, 4)], [(2, 2), (2, 4)], [(3, 0), (3, 2)], [(2, 5), (2, 3)], [(5, 4), (3, 4)], [(4, 6), (4, 4)], [(3, 4), (5, 4)], [(6, 4), (4, 4)], [(2, 0), (2, 2)], [(4, 3), (4, 5)], [(4, 1), (4, 3)], [(2, 6), (4, 6)], [(3, 2), (1, 2)], [(6, 2), (4, 2)], [(4, 6), (4, 4)], [(4, 3), (4, 1)], [(0, 2), (2, 2)], [(2, 2), (2, 4)], [(1, 4), (3, 4)], [(3, 4), (5, 4)], [(6, 3), (4, 3)], [(4, 0), (4, 2)], [(4, 2), (4, 4)], [(5, 4), (3, 4)], [(3, 5), (3, 3)]]
Pins in  1.0
     0    1  2  3  4    5    6
0  NaN  NaN  0  0  0  NaN  NaN
1  NaN  NaN  0  0  0  NaN  NaN
2  0.0  0.0  0  0  0  0.0  0.0
3  0.0  0.0  0  1  0  0.0  0.0
4  0.0  0.0  0  0  0  0.0  0.0
5  NaN  NaN  0  0  0  NaN  NaN
6  NaN  NaN  0  0  0  NaN  NaN