# life.py - Once complete, this program will play the game of
#           life.

# Need to import several modules.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# The update function is needed for the animation
#   to work properly. It has four parameters:
# frameNum - this is handled by the animation, don't change this.
# img - the plot that is passed and changed, don't change this.
# world - the two-D array that represents the world for the
#         game of life. This will be updated to the next gen.
# N - the size of the world (which is square).

def update( frameNum, img, world, N ) :

    # This line copies the current cells into newWorld.
    newWorld = world.copy( )

    ## TODO - Write code here to update the cells in newWorld
    ##        for the next generation of life. Remember to
    ##        use the toroidal model. Rather than making
    ##        special cases for row/column 0 and N-1, just
    ##        use the % operator.
    
    for i in range(N) :

        for j in range(N) :
            aliveCount = 0
            
            if newWorld[(i-1)%N][(j-1)%N] == 255 :
                aliveCount += 1
                    
            if newWorld[(i-1)%N][j] == 255 :
                aliveCount += 1

            if newWorld[i][(j-1)%N] == 255 :
                aliveCount += 1

            if newWorld[i][(j+1)%N] == 255 :
                aliveCount += 1

            if newWorld[(i+1)%N][j] == 255 :
                aliveCount += 1
                
            if newWorld[(i+1)%N][(j+1)%N] == 255 :
                aliveCount += 1
                    
            if newWorld[i][j] == 255:

                if aliveCount < 2 :
                    newWorld[i][j] = 0
                elif aliveCount > 3 :
                    newWorld[i][j] = 0
                else :
                    newWorld[i][j] = 255

            else :

                if aliveCount == 3 :
                    newWorld[i][j] = 255
                else :
                    newWorld[i][j] = 0
    # This code changes the data in the plot to be the
    #   new world's data. Then we set world to be
    #   newWorld, then we return img.
    #
    # Do not change this code, or the animation may not
    #   work. Make sure newWorld is completely calculated
    #   before you get to this point.
    img.set_data( newWorld )
    world[:] = newWorld[:]
    return img




# Beginning of main program.

# Note - this code assumes that the grid is a two-dimensional
#   numpy array object named world. Do not change the name of
#   this variable.

# N represents the size of the world - it is an N x N grid.
#   Any value will work here, although if you get around
#   200 or higher, it will be pretty laggy. 100 seems to
#   work pretty well.
N = 100

# SPEED represents the number of milliseconds between
#   generations of the game. The higher the number, the
#   slower the game will update. I would not go much
#   lower than 20.
SPEED = 500

# PROB_LIFE represents the probability that a cell will
#   start the game alive. It should be an integer between
#   0 and 100, representing a percentage chance.
PROB_LIFE = 30


## TODO - Write code here to create the initial population
##   of the world. I recommend creating an N x N array that
##   is initially filled with random numbers from 0 to 99.
##   Then use the PROB_LIFE to change the entries to be
##   either alive (255) or dead (0).

world = np.array( [ [random.randint(0,99) for i in range(N)] for j in range(N) ] )
print(world)

for i in range(N) :
    
    for j in range(N) :
        
        if world[i][j] < PROB_LIFE :
            world[i][j] = 255
        else :
            world[i][j] = 0


# The following code is necessary to set up the display and
#   make the animation happen. Do not change any code below
#   this comment, or it may not work.
fig, ax = plt.subplots( )
img = ax.imshow( world, interpolation='nearest' )
ani = animation.FuncAnimation( fig, update, fargs = ( img, world, N ),
                               frames = 10, interval = SPEED,
                               save_count = 50 )
plt.show( )

# This is the end of the program. You should not need
#   anything after this point.
