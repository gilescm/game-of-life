# Game of Life

# Table of Contents
1. [Description](#description)
2. [How to Run](#how-to-run)
3. [Dependencies](#dependencies)

## Description
A Python Program that simulates Conway's Game of Life. When run, a window is created displaying a board on which the Game Of Life is run. The board is initialised by default as a square grid of 100x100 cells, each cell has a 20% of initialising alive. This board will iterate to infinity, applying the rules for the Game Of Life between each iteration. Provided `argparse` is installed the board size can be configured with the command line argument `--grid-size=50`.

This is also true for the type of board initialised. By default a toroidal board is created, i.e. a board that wraps around itself, cells at the edges of the board are neighbours to cells at the same height/width on the opposite edge of the board. The board can be switched to an infinite board by passing in the argument `--infinite=True` next to `python main.py` and any other arguments passed in.
When using an infinite board, it will initialise as a standard board, but when an alive cell is found at any edge, the board will grow on all sides by one row during the next iteration. The new cells will all be dead at initialisation and then the Game of Life rules are applied to them.

It is also possible to define an initial _"seed"_ board for the Game Of Life. This can be done by passing in the command line argument `--seed=random`. Details of available seeds can be found below. Currently the only available seeds are `random` which initialises a randomise board and `blinker` which initialises a row of 3 live cells in the centre of the board. If you would like to decrease/increase the time between iterations you can pass in the argument `--interval=50` where `50` is the milliseconds between iterations.

## How to Run
You can run this program by downloading this repository and running the following command from your console in the repositorys folder
```
python main.py
```
### Optional Arguments
If have the python package argparse you can add the following arguments to the command that change the parameters for this Game of Life:
- `--grid-size`:
  - **Default =**`100`
  - This defines the size of the grid the game of life takes place upon
  
- `--infinite`
  - **Default =**`'False'`
  - If this argument is set to `'True'` then the grid will simulate an infinite grid by growing the grid when an alive cell if found at any edge.
- `--seed`
  - **Default =**`'random'`
  - This argument currently accepts the following: 
    - `'blinker'` sets up the initial grid completely empty except for a line of 3 alive cells in the centre of the board
- `--interval`
  - **Default =**`50`
  - This argument sets the interval in milliseconds between frames for the animation

## Dependencies
This program requires the `numpy` and `matplotlib` packages to run and is enhanced with some command line arguments if `argparse` is installed. You can install these dependencies by running the command below or installing each one individually. 
```
python dependencies.py
```

#### argparse
Optional but required to pass command line arguments. Install with:
````
pip install argparse
````
#### numpy
Required for the Game of Life's grid manipulation. Install with:
````
pip install numpy
````
#### matplotlib
Required to initialise and display an animation for this Game of Life. Install with:
````
pip install matplotlib
````
