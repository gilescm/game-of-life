# Neighbours()
# Calculates how many currently alive neighbours a cell at i,j has
def Neighbours(i, j, grid, N, Infinite):
    
    if Infinite is False:
        Total = WrappedTotal(i, j, grid, N)
    else:
        Total = InfiniteTotal(i, j, grid)
    
    # print(Total)
    return Total 

##################
# Helper Functions

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