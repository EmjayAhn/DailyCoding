# given a number n, draw stairs with 'I' n tall and n wide,
# with the tallest in the top left.
# Example (with - to represent spaces;
# DO NOT USE THEM IN THE SOLUTIONS!
# USE SPACES IN SOLUTION!
# the "-"s are for clarity.)
# draw_stairs(3) == '''I\n_I\n__I'''

#codewars 8kyu

def draw_stairs(n):
    # do something
    wide = ' '
    result = ""
    for index in range(n):
        result += index * wide + 'I'
        if index != n - 1:
            result += '\n'

    return result
