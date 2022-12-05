from copy import deepcopy
from functools import reduce
from itertools import takewhile
from parse import parse
from utils import get_input


#######################
# mark: INPUT PARSING #
#######################


lines = get_input('day5')

ship = list(takewhile(lambda x: x != '', lines))
inst = lines[len(ship) + 1:]


def build_ship_arr(ship_lines):
    """ Parse the lines for the ship into an array of strings.

    Each string denotes the contents of the corresponding boat.

    """
    ships = []
    for i in range((len(ship_lines[-1]) // 4) + 1):
        ships.append('')
    ship_lines = ship_lines[:-1]

    for s in ship_lines:
        for i in range(0, len(s), 4):
            char = s[i + 1]
            if char != ' ':
                ships[i // 4] = char + ships[i // 4]
    return ships


def build_inst_arr(inst_lines):
    """ Parse the lines for the instructions into instruction tuples.

    Each tuple represents (move_amt, from_ship, to_ship)

    """
    def p(s):
        parse('move {:d} from {:d} to {:d}', s)
    res = list(map(p, inst_lines))
    return res


######################
# mark: PROBLEM CODE #
######################


def stack_move(inst, ship_arr):
    """ Execute move instruction in a FILO fashion """
    n, j, k = inst
    for i in range(n):
        ship_arr[k - 1] += ship_arr[j - 1][-1]
        ship_arr[j - 1] = ship_arr[j - 1][:-1]


def queue_move(inst, ship_arr):
    """ Execute move instruction in a FIFO fashion """
    n, j, k = inst
    ship_arr[k - 1] += ship_arr[j - 1][-n:]
    ship_arr[j - 1] = ship_arr[j - 1][:-n]


def get_res(ship_arr, inst_arr, move_method):
    """ Get the resulting ship string when executing the instructions with a
    given method.

    @param ship_arr    Array detailing which ships store what crates as a string 
    @param inst_arr    Instruction array containing move instruction tuples
    @param move_method Method for enacting the move instructions for inst_arr on
                       ship_arr
    @return Crate on top of each ship, concatenated together.

    """
    sa = deepcopy(ship_arr)
    for i in inst_arr:
        move_method(i, sa)

    return reduce(lambda x, s: x + s[-1], sa)


ship_arr = build_ship_arr(ship)
inst_arr = build_inst_arr(inst)

print(get_res(ship_arr, inst_arr, stack_move),
      get_res(ship_arr, inst_arr, queue_move))
