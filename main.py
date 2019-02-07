# Imports / Includes
import argparse
import numpy as Num 
import matplotlib.pyplot as Plot  
import matplotlib.animation as Animation 
from   matplotlib.widgets import Button

import State as S

# Constants / Literals
ON      = 1
OFF     = 0

# Evolve()
# Conducts one iteration on our game of life state, creating a new grid if necessary
# and applies rules to the cells of the grid 
def Evolve(frameNum, img, objState):

    NextState(objState) 
    NewGrid = ApplyRules(objState)

    img.set_data(NewGrid)
    objState.grid = NewGrid
    return img

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
    if Infinite is True:
        N  = objState.length - 1 
    else:
        N  = objState.length

    for i in range(N): 
        for j in range(N):
            # Cell in question
            Cell  = objState.grid[i, j]

            # Total Alive Neighbours
            Total = Neighbours(i,j, objState.grid, N, Infinite)

            if Cell == ON: 
                # Underpopulation and Overcrowding
                if (Total < 2) or (Total > 3): 
                    NewGrid[i, j] = OFF 
            else: 
                # Creation of Life
                if Total == 3: 
                    NewGrid[i, j] = ON 
    return NewGrid

# Neighbours()
# Calculates how many currently alive neighbours a cell at i,j has
def Neighbours(i, j, grid, N, Infinite):
    
    if Infinite is False:
        Total = WrappedTotal(i, j, grid, N)
    else:
        Total = InfiniteTotal(i, j, grid)
    
    # print(Total)
    return Total 

# WrappedTotal()
# Calculates and returns the total number of alive neighbours for a cell on a grid
# that wraps around itself
def WrappedTotal(i, j, grid, N):
    Total = 0

    Total += grid[(i-1)%N, (j-1)%N] # Top Left
    Total += grid[i      , (j-1)%N] # Top Mid
    Total += grid[(i+1)%N, (j-1)%N] # Top Right
    Total += grid[(i-1)%N, j      ] # Mid Left
    Total += grid[(i+1)%N, j      ] # Mid Right
    Total += grid[(i-1)%N, (j+1)%N] # Bot Left
    Total += grid[i      , (j+1)%N] # Bot Mid
    Total += grid[(i+1)%N, (j+1)%N] # Bot Right

    return Total

# InfiniteTotal()
# Calculates and returns the total number of alive neighbours for a cell
def InfiniteTotal(i, j, grid):
    Total = 0

    Total += grid[(i-1), (j-1)] # Top Left
    Total += grid[i    , (j-1)] # Top Mid
    Total += grid[(i+1), (j-1)] # Top Right
    Total += grid[(i-1), j    ] # Mid Left
    Total += grid[(i+1), j    ] # Mid Right
    Total += grid[(i-1), (j+1)] # Bot Left
    Total += grid[i    , (j+1)] # Bot Mid
    Total += grid[(i+1), (j+1)] # Bot Right

    return Total

def Arguments():

    # parse arguments 
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.") 

    # add arguments 
    parser.add_argument('--grid-size', dest='N', required=False) 
    parser.add_argument('--infinite', dest='Infinite', required=False) 
    parser.add_argument('--interval', dest='Interval', required=False) 
    parser.add_argument('--seed', dest='Seed', required=False) 
    args = parser.parse_args() 
        
    # Set Grid size 
    N = 100
    if args.N and int(args.N) > 8: 
        N = int(args.N) 
            
    # Set state of grid. Either Infinite or wrapped
    # If the grid is infinite then it will grow if a live cell if found at any edge 
    Infinite = False
    AcceptedTerms = ['True', 'true', 'On', 'on', 'Yes', 'yes', 'Y', '1']
    if args.Infinite in AcceptedTerms: 
        Infinite = True

    # Set the seed for the grid's initial state 
    Seed = 'random'
    AcceptedTerms = ['blinker', 'empty', 'void', 'none', 'dead', '0']
    if args.Seed and args.Seed in AcceptedTerms: 
        Seed = args.Seed 
            
    # Set the animation's update interval 
    Interval = 50
    if args.Interval and args.Interval > 0: 
        Interval = int(args.Interval) 

    return [N, Infinite, Interval, Seed]

# Main()
# Our main function that runs the show
def Main(): 

    N, Infinite, Interval, Seed = Arguments()
    objState = S.State(N, Infinite=Infinite, Seed=Seed)
    
    # Set up animation 
    updateInterval = 50
    fig, ax = Plot.subplots() 
    img = ax.imshow(objState.grid, interpolation='nearest') 
    ani = Animation.FuncAnimation(fig, Evolve, fargs=(img, objState), 
                                  frames = 100, 
                                  interval=Interval, 
                                  save_count=50) 
  
    Plot.show() 
 
if __name__ == '__main__': 
    Main() 