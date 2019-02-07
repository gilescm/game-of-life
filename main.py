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

    AcceptedInfinites = ['True', 'true', 'On', 'on', 'Yes', 'yes', 'Y', '1']
    AcceptedSeeds     = ['blinker', 'empty', 'void', 'none', 'dead', '0']

    Text = {
        'grid_size': 'An integer N that defines the initial size of the NxN square grid',
        'infinite' : 'If any of the following then the Game Of Life will be run on a grid of infinite size',
        'interval' : 'An integer N that defines the time gap in milliseconds between frames when animating the Game Of Life',
        'seed'     : 'A string value that dictates which seed to use for the initial grid the Game Of Life will be played on'
    }

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.") 
    parser.add_argument('--grid-size', dest='N', required=False, help=Text['grid_size']) 
    parser.add_argument('--infinite', dest='Infinite', required=False, choices=AcceptedInfinites, help=Text['infinite']) 
    parser.add_argument('--interval', dest='Interval', required=False, help=Text['interval']) 
    parser.add_argument('--seed', dest='Seed', required=False, choices=AcceptedSeeds, help=Text['seed']) 

    args = parser.parse_args() 
        
    # Set Grid size 
    N = 100
    if args.N and int(args.N) > 8: 
        N = int(args.N) 
            
    # Set state of grid. Either Infinite or wrapped
    # If the grid is infinite then it will grow if a live cell if found at any edge 
    Infinite = False
    if args.Infinite in AcceptedInfinites: 
        Infinite = True

    # Set the seed for the grid's initial state 
    Seed = 'random'
    if args.Seed and args.Seed in AcceptedSeeds: 
        Seed = args.Seed 
            
    # Set the animation's update interval 
    Interval = 50
    if args.Interval and args.Interval > 0: 
        Interval = int(args.Interval) 

    return [N, Infinite, Interval, Seed]

 
if __name__ == '__main__': 
    Main() 