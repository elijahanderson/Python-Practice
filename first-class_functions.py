# First-Class Functions


def square(x) :
    return x*x

def cube(x) :
    return x*x*x

f = square(5)

# You can actually take out the passing of the argument -- set the var to the function without executing it
g = square

print(f)
print(square)
# print(g) prints the same thing as print(square)
print(g)
print(g(5))

# Python's map() function takes a function and a list as arguments, runs each value of that list through the function,
# and returns a new array of the results
# This is Python's map() function, except built from scratch to understand what's going on

def my_map(func, arg_list) :
    result = []
    for i in arg_list :
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])

print(squares)

# So we can pass any function we want into the map
cubes = my_map(cube, [1,2,3,4,5])

print(cubes)

# You can also return functions as the result of other functions

def logger(msg) :

    def log_message() :
        print('Log: ', msg)

    return log_message

# set log_hi equal to the logger function, with 'Hi' as the argument
# since logger() returns log_message without executing it, log_hi is therefore set to the function log_message()
log_hi = logger('Hi')
log_hi()
