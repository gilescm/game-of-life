# 3rd Party Imports / Includes
import argparse
import matplotlib.pyplot as Plot  
import matplotlib.animation as Animation 
from   matplotlib.widgets import Button

# Imports / Includes
import State as S
import Iteration as I

# Main()
# Our main function that runs the show
def Main(): 

    N, Infinite, Interval, Seed = Arguments()
    objState = S.State(N, Infinite=Infinite, Seed=Seed)
    
    # Set up animation 
    fig, ax = Plot.subplots() 
    img = ax.imshow(objState.grid, interpolation='nearest') 
    ani = Animation.FuncAnimation(fig, I.Iterate, fargs=(img, objState), 
                                  frames = 100, interval=Interval) 
  
    Plot.show() 

# Arguments()
# This is where we define defaults for and set arguments passed in through the
# command line
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

 
if __name__ == '__main__': 
    Main() 