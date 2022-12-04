from utils import solve_sum_problem, get_input
import re


sections = get_input('day4')


def parse(line):
    secs = re.split('[,-]', line)
    return tuple(secs)


# Part 1

def range_contains(tup):
    r1s, r1e, r2s, r2e = (int(x) for x in tup)
    return ((r1s <= r2s) and (r2e <= r1e)) or ((r2s <= r1s) and (r1e <= r2e))


sol_1 = solve_sum_problem(range_contains, parse, sections)


# Part 2

def range_overlaps(tup):
    r1s, r1e, r2s, r2e = (int(x) for x in tup)
    return r1s <= r2s <= r1e or r1s <= r2e <= r1e or r2s <= r1s <= r2e or r2s <= r1e <= r2e


sol_2 = solve_sum_problem(range_overlaps, parse, sections)


print(sol_1, sol_2)
