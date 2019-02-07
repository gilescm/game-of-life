# Game Of Life

### Table of Contents
1. [Description](#description)
2. [Assumptions](#assumptions)
2. [Rules](#rules)
3. [How to Run](#how-to-run)
4. [Dependencies](#dependencies)

## Description
A Python Program that simulates Conway's Game Of Life. When run, a window is created displaying a board on which the Game Of Life is run. The board is initialised by default as a square grid of 100x100 cells, each cell with a 30% of initialising alive, applying the rules (See [Rules](#rules) below) for the Game Of Life between each iteration. By default a toroidal board is created, i.e. a board that wraps around itself. Cells at the edges of the board are neighbours to cells at the same height/width on the opposite edge of the board. The board can be switched to an infinite board by passing in the argument `--infinite=True` next to `python main.py` and any other arguments passed in. When using an infinite board, it will initialise as a standard board, but when an alive cell is found at any edge, the board will grow on all sides by one row during the next iteration. The new cells are dead at initialisation and then the Game Of Life rules are applied to them.

It is also possible to define an initial _"seed"_ board for the Game Of Life. This can be done by passing in the command line argument `--seed=random`. Details of available seeds can be found below. Currently the only available seeds are `random` which initialises a randomise board and `blinker` which initialises a row of 3 live cells in the centre of the board. If you would like to decrease/increase the time between iterations you can pass in the argument `--interval=50` where `50` is the milliseconds between iterations. _(See [Optional Arguments](#optional-arguments) below for further details.)_

## Assumptions

- It is assumed that at any point any given cell in the square grid is either alive or dead. _(Note: This is represented in the code as ON=1 or OFF=0.)_ 
- This default initialisation of the board for this Game Of Life is a toroidal grid, one that wraps around itself. This is the default assumption as it can be argued that a grid that wraps left to right and top to bottom is in itself infinite, it is also less intensive graphically when run for longer periods of time than a true infinite board. However, if you would like to run the Game Of Life on an infinite board then you can pass the command line argument `--infinite=True`.
- A cells neighbours are assumed to be the cells that are horizontally, vertically or diagonally adjacent to it.

## Rules

This Game Of Life applies the following rules to each cell in the grid between iterations:
- **Rule 0: No Interactions** If a cell is dead and all its neighbours are dead then the cell will stay dead on the next iteration
- **Rule 1: Underpopulation** If a cell is alive and has less than two alive neighbours then it will die on the next iteration
- **Rule 2: Overcrowding** If a cell is alive and has more than three alive neighbours then it will die on the next iteration
- **Rule 3: Survival** If a cell is alive and has two or three alive neighbours then it will die on the next iteration
- **Rule 4: Creation Of Life** If a cell is dead and has exactly three alive neighbours then it will become alive on the next iteration

## How to Run
You can run this program by downloading this repository and running the following command from your console in the repositorys folder
```
python main.py
```
### Optional Arguments
If have the python package `argparse` you can add the following arguments to the command that change the parameters for this Game Of Life:
- `--grid-size`
  - **Default =**`100`
  - This defines the size of the grid the Game Of Life takes place upon, must be an integer.
  
- `--infinite`
  - **Default =**`'False'`
  - If this argument is set to `'True'` then the grid will simulate an infinite grid by growing the grid when an alive cell if found at any edge.
  - You can also use any of the following to initialise an infinite grid: `'true'`, `'Yes'`, `'yes'`, `'On'`, `'on'`,`'Y'`,`'1'`
- `--seed`
  - **Default =**`'random'`
  - This argument currently accepts the following: 
    - `'blinker'` sets up the initial grid with one line of 3 alive cells in the centre of the board
    - `'empty'` sets up the initial grid completely empty, you can also use `'void'`, `'none'`, `'dead'` and `'0'` as alternatives to `'empty'`.
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
Required for the Game Of Life's grid manipulation. Install with:
````
pip install numpy
````
#### matplotlib
Required to initialise and display an animation for this Game Of Life. Install with:
````
pip install matplotlib
````
