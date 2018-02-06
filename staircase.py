"""
    A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps
    at a time.
    Implement a method to count how many possible ways the child can run up the stairs.
"""
def staircase(num_stairs) :
    # if there are 1-3 steps, it's easy to determine the number of ways the you can climb them
    if num_stairs == 1 :
        return 1
    if num_stairs == 2 :
        return 2
    if num_stairs == 3 :
        return 4
    # otherwise, call the function recursively for each amount of steps the kiddo can take next
    else :
        return staircase(num_stairs-3) + staircase(num_stairs-2) + staircase(num_stairs-1)

print('6 stairs: ' + str(staircase(6)))
print('20 stairs: ' + str(staircase(20)))

