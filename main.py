"""
Solitaire

This script features a brute force method of solving the game of 'Solitaire' by randomly selecting one the legal moves,
 and moving, then looking at new legal moves, selection one at random and continuing.

More advanced methods will be implemented in the future.


=============
Input: None
Output: printed output in console
=============

"""

import numpy as np
import pandas as pd
import time

import warnings
warnings.filterwarnings("ignore")


def pandas_wide():
    # import pandas as pd
    desired_width = 200
    pd.set_option('display.width', desired_width)
    # For series
    pd.set_option('display.max_seq_items', None)
    # For DataFrame columns
    pd.set_option('display.max_columns', None)


def init(spec: dict):
    """
    Initiate the game grid with empty holes as 0 and pins as 1, as well as invalid positions as np.nan types.

    :param spec: dict
    :return: pd.DataFrame object
    """

    l1 = [np.nan, np.nan, 1, 1, 1, np.nan, np.nan]
    l2 = [np.nan, np.nan, 1, 1, 1, np.nan, np.nan]
    l3 = [1, 1, 1, 1, 1, 1, 1]
    l4 = [1, 1, 1, 0, 1, 1, 1]
    l5 = [1, 1, 1, 1, 1, 1, 1]
    l6 = [np.nan, np.nan, 1, 1, 1, np.nan, np.nan]
    l7 = [np.nan, np.nan, 1, 1, 1, np.nan, np.nan]

    a = [l1, l2, l3, l4, l5, l6, l7]
    a = pd.DataFrame(a)
    if spec["verbose"]:
        print(a)
        print(f"Pins in \t {np.sum(np.sum(a))}")
    return a


def find_all_zeroes(a, spec: dict, search_target=0):
    """
    Find the coordinates of each location where there is no pin (== 0) and put the coordinates into a list.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :param search_target: which target value you want to identiy
    :return: list
    """
    x, y = list(np.where(a == search_target)[1]), list(np.where(a == search_target)[0])
    positions_zeroes = list(zip(x, y))
    if spec["verbose"]:
        print(f"There are {len(positions_zeroes)} empty position(s) \t{positions_zeroes}")
    return positions_zeroes


def find_all_moves(a, spec: dict, positions_zeroes: list):
    """
    Find the coordinates of all legal moves and put them into a list.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :param positions_zeroes: list, all positions that are empty at the moment
    :return: list, of all legal moves
    """
    # find all possible moves
    all_moves = []
    for zero in positions_zeroes:
        bounds = (0, 6)

        # checking y coordinates
        if 0 <= zero[0] + 2 <= 6 and (not np.isnan(a[zero[0] + 2][zero[1]])) and a[zero[0] + 2][zero[1]] != 0 and a[zero[0] + 1][zero[1]] == 1:
            all_moves.append([(zero[0] + 2, zero[1]), zero])
        if 0 <= zero[0] - 2 <= 6 and (not np.isnan(a[zero[0] - 2][zero[1]])) and a[zero[0] - 2][zero[1]] != 0 and a[zero[0] - 1][zero[1]] == 1:
            all_moves.append([(zero[0] - 2, zero[1]), zero])

        # checking x coordinates
        if 0 <= zero[1] + 2 <= 6 and (not np.isnan(a[zero[0]][zero[1] + 2])) and a[zero[0]][zero[1] + 2] != 0 and a[zero[0]][zero[1] + 1] == 1:
            all_moves.append([(zero[0], zero[1] + 2), zero])
        if 0 <= zero[1] - 2 <= 6 and (not np.isnan(a[zero[0]][zero[1] - 2])) and a[zero[0]][zero[1] - 2] != 0 and a[zero[0]][zero[1] - 1] == 1:
            all_moves.append([(zero[0], zero[1] - 2), zero])

    if len(all_moves) > 0:
        if spec["verbose"]:
            print(f"All legal moves \t {all_moves}")
        spec["legal_moves"] = True

    else:
        assert len(all_moves) == 0
        if spec["verbose"]:
            print(f"No legal moves found!")
        spec["legal_moves"] = False

    return all_moves


def chose_move(spec, all_moves: list, how: str):
    """
    Chose one of the legal moves provided from the list 'all_moves'.

    :param spec: dict, specifications dictionary for modifying the program
    :param all_moves: list, all legal moves
    :param how: str, chose a method to determine the next move, so far: ['random', 'first']
    :return: list, containing one element - the selected move, subset of the legal move items
    """
    if how == 'random':
        # randomly chose one
        rand = np.random.randint(len(all_moves))
        selected_move = all_moves[rand]
        if spec["verbose"]:
            print(f"Selected move \t{selected_move}")
    elif how == 'first':
        # chose first
        selected_move = all_moves[0]
        if spec["verbose"]:
            print(f"Selected move \t{selected_move}")
    else:
        raise Exception("Unknown operational mode. Chose 'random' or 'random'.")

    assert len(selected_move) == 2, f"Expected to only select 2 moves (start, end), but found {len(selected_move)}."

    return selected_move


def move(a, spec: dict, selected_move: list):
    """
    Perform the 'selected_move'.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :param selected_move: list, containing one element
    :return: 0
    """

    old = selected_move[0]
    new = selected_move[1]

    if spec["verbose"]:
        print(f"Move is from {old} to {new}.")

    # perform selected_move by changing the array entries
    a[old[0]][old[1]] = 0
    a[new[0]][new[1]] = 1
    if old[0] == new[0] and old[1] == new[1]:
        raise Exception("Old and new coordinates are the same!")
    if old[0] == new[0]:

        a[old[0]][np.mean([old[1], new[1]])] = 0
    if old[1] == new[1]:
        a[np.mean([old[0], new[0]])][old[1]] = 0

    move_list = spec["move_list"]
    move_list.append(selected_move)
    if spec["verbose"]:
        print(f"The following moves were made so far \t{move_list}")
        print(a)
    return 0


def evaluate_end(a, spec: dict):
    """
    Determine whether the end conditions are met or not.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :return: 0
    """
    pins_in = np.sum(np.sum(a))
    pin_out = spec["pins_start"] - pins_in
    if spec["verbose"]:
        print(f"Pins in board \t{pins_in} \t\t Pins taken out \t{pin_out}")

    if pins_in >= 2:
        if pins_in < spec["pins_last_iter"]:
            if spec["verbose"]:
                print(f"{pins_in} pins remaining. Continuing...\n\n")
            spec["pins_last_iter"] = pins_in
        else:
            assert pins_in == spec["pins_last_iter"]
            if spec["verbose"]:
                print("No further progress - the number of pins is not changing.")
            spec["reset"] = True

            if spec["run_limit"] == spec["iteration"]:
                spec["running"] = False
                print(f"Iteration {spec['run_limit']} reached. Terminating")

    else:
        # only 1 pin in board
        assert pins_in == 1
        spec["running"] = False
        print("Solution with one pin found!")
        if True:
            print("Pins in\t", spec["pins in"])
            print("Move list\t", spec["move_list"])
            print(a)

    return 0


def save_run(a, spec: dict):
    """
    Save the current 'run' to a dictionary.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :return: 0
    """
    if spec["reset"] or not spec["running"]:
        all_move_hist = spec["all_move_hist"]
        all_move_hist.append({
            "iteration": spec["iteration"],
            "move_list": spec["move_list"],
            "board": a,
            "pins_in": np.sum(np.sum(a))
        })

        spec["iteration"] = spec["iteration"] + 1

        if spec["verbose"]:
            print("Iteration\t\t", spec["iteration"])
            print("Saving run ...")

        if spec["iteration"] % 100 == 0:
            print(f"Iteration\t\t{spec['iteration']}\t\t\t\t"
                  f"Time\t\t{round((time.time() - spec['start_time']) / 60, 1)}\tmin")
            time.sleep(.5)

    return 0


def reset_board(a, spec: dict):
    """
    Reset the board and all parameters to initial conditions.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :return: 0
    """
    if spec["reset"]:
        a = init(spec)
        spec["move_list"] = []
        spec["pins_last_iter"] = np.inf
        spec["board"] = np.nan
        spec["reset"] = False
        if spec["verbose"]:
            print("Resetting board ...")
    return a


def present_results(spec):
    """
    Results of the final findings are printed out-

    :param spec: dict, specifications dictionary for modifying the program
    :return: 0
    """
    df = spec["all_move_hist"]
    df = pd.DataFrame(df)
    print(df)
    return 0


def start_iterations(a, spec: dict):
    """
    Iterative loop where zero positions are determined, legal moves are determined, moves chosen and then
    the end conditions are evaluated and data is safed and the board reset.

    :param a: pd.DataFrame object, the game grid
    :param spec: dict, specifications dictionary for modifying the program
    :return: 0
    """

    while spec["running"]:
        position_zeroes = find_all_zeroes(a, spec)
        all_moves = find_all_moves(a, spec, position_zeroes)
        if spec["legal_moves"]:
            selected_move = chose_move(spec, all_moves, "random")
            move(a, spec, selected_move)
        evaluate_end(a, spec)
        save_run(a, spec)
        a = reset_board(a, spec)
    return 0


def main():
    pandas_wide()

    spec = {
        "running": True,
        "reset": False,
        "legal_moves": False,
        "iteration": 0,
        "run_limit": np.nan,
        "move_list": [],
        "pins_last_iter": np.inf,
        "all_move_hist": [],
        "board": np.nan,
        "verbose": False,
        "start_time": time.time()
    }

    a = init(spec)
    spec["pins_start"] = np.sum(np.sum(a))

    start_iterations(a, spec)
    present_results(spec)
    return 0


if __name__ == '__main__':
    main()
