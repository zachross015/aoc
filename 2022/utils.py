def solve_sum_problem(predict, modify, input):
    """ Reduces boilerplate pipeline for typical AOC code.

    Problems typically follow the pipeline of take an input, modify it in some
    way, use this modification to predict an outcome. This reduces the boiler
    plate where the solution involves summing the results.

    @param predict Function who takes the `modify` output and predicts a
    solution.  @param modify  Modifies each entry in `input` via 1-1 mapping.
    @param input   The pre-processed program input.  @return Program solution.
    """
    return sum(map(predict, map(modify, input)))


def get_input(file):
    # Read Inputs
    with open(f'inputs/{file}') as f:
        return f.read().splitlines()
