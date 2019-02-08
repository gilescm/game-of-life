# 3rd Party Imports / Includes
import numpy as Num 

# Imports / Includes
import RuleHelpers as H

# Constants / Literals
ON      = 1
OFF     = 0

# Iterate()
# Conducts one iteration on our game of life state, creating a new grid if necessary
# and applies rules to the cells of the grid 
def Iterate(frameNum, img, objState):

    NextState(objState) 
    NewGrid = ApplyRules(objState)

    img.set_data(NewGrid)
    objState.grid = NewGrid
    return img


###################
# Iteration Helpers

# NextState()
# Returns the next state our game will be in before cells survive/live/die.
# This new state checks the edges and extends the grid if necessary
def NextState(objState):
    NewGrid     = objState.grid.copy()
    N           = objState.length
    EdgesToGrow = objState.EdgeCase()

    if EdgesToGrow:
        VerticalRow   = Num.zeros(N) 
        HorizontalRow = Num.zeros(N+2).reshape(N+2,1) 
        NewGrid = Num.vstack((VerticalRow,NewGrid))
        NewGrid = Num.vstack((NewGrid, VerticalRow))
        NewGrid = Num.hstack((HorizontalRow, NewGrid))
        NewGrid = Num.hstack((NewGrid, HorizontalRow))
        N = N + 2

    objState.grid   = NewGrid
    objState.length = N

    return objState

# ApplyRules()
# Apply Scenarios 0 through 4 to each cell on the grid
# Returns a new grid with those rules applied
def ApplyRules(objState):
    NewGrid   = objState.grid.copy()
    Infinite  = objState.isInfinite

    # If we are using an Infinite grid then we need make sure we do not
    # performs calculations on cells outside of the grid
    if Infinite:
        N  = objState.length - 1 
    else:
        N  = objState.length

    for i in range(N): 
        for j in range(N):
            # Cell in question
            Cell  = objState.grid[i, j]

            # Total Alive Neighbours
            Total = H.Neighbours(i,j, objState.grid, N, Infinite)

            if Cell == ON: 
                # Underpopulation and Overcrowding
                if (Total < 2) or (Total > 3): 
                    NewGrid[i, j] = OFF 
            else: 
                # Creation of Life
                if Total == 3: 
                    NewGrid[i, j] = ON 
    return NewGrid
