# Game of Life

# Table of Contents
1. [Description](#description)
2. [How to Run](#how-to-run)
3. [Dependencies](#dependencies)

## Description
A Python Program that simulates Conway's Game of Life. This program requires the `numpy` and `matplotlib` packages to run and is enhanced with some command line arguments if `argparse` is installed. You can install these dependencies by running the command below. _(See also [Dependencies](#dependencies) for individual descriptions/reasons why necessary and download commands.)_ 
```
python dependencies.py
```

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
    - `'blinker'` sets up the initial grid completely empty except for a line of 3 alive cells in the center
- `--interval`
  - This argument sets the interval between frames for the animation

## Dependencies
In order to run this python program you will need to install the following dependencies if you do not already have them on your machine.

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
