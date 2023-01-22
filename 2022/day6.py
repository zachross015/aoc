from utils import get_input

inp = get_input('day6')
print(inp)

def find_idx(string, num_chars):

    # Dictionary for maintaining the count of each character
    counts = {}

    for i in range(0, len(string)):

        # Append the character or add to the count
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1

        if i >= num_chars:
            counts[string[i - num_chars]] -= 1

            # Remove the character if it hasn't occured within the last
            # `num_chars`.
            if counts[string[i - num_chars]] <= 0:
                del counts[string[i - num_chars]]

            # Otherwise, if all the counts are unique then return
            if len(counts) == num_chars:
                return (i + 1) 

# Go through each line and fine the answer for 4 and 14 (part 1, part 2)
for string in inp:
    print(find_idx(string, 4), find_idx(string, 14))
