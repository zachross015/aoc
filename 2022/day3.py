# Read Inputs
with open("inputs/day3") as f:
    rucksacks = f.read().splitlines()

def convert(char):
    """ Convert a-Z to the range 1-52 """
    val = ord(char)
    return val - 96 if val > 96 else val - 38

def solve_sum_problem(predict, modify, input):
    """ Reduces boilerplate pipeline for typical AOC code.
    
    Problems typically follow the pipeline of take an input, modify it in some way, use this modification 
    to predict an outcome. This reduces the boiler plate where the solution involves
    summing the results.

    @param predict Function who takes the `modify` output and predicts a solution.
    @param modify  Modifies each entry in `input` via 1-1 mapping.
    @param input   The pre-processed program input.
    @return Program solution.
    """
    return sum(map(predict, map(modify, input)))


# Part 1 #

bags = [(set(a[:(len(a) // 2)]), set(a[(len(a) // 2):])) for a in rucksacks]
common_2 = lambda tup: ''.join(tup[0].intersection(tup[1]))

sol_1 = solve_sum_problem(convert, common_2, bags)


# Part 2

triples = [(set(rucksacks[i]), set(rucksacks[i + 1]), set(rucksacks[i + 2])) for i in range(0, len(bags), 3)]
common_3 = lambda tup: ''.join(tup[0].intersection(tup[1].intersection(tup[2])))

sol_2 = solve_sum_problem(convert, common_3, triples)

print(sol_1, sol_2)
