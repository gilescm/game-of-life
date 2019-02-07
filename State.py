import numpy as Num 

# Constants / Literals
ON      = 1
OFF     = 0

class State:

    Values  = [ON, OFF]
    
    # Initializer / Instance Attributes
    def __init__(self, N, Seed='random', Infinite=False):

        self.length     = N
        self.grid       = Num.random.choice(self.Values, self.length*self.length, p=[0, 1]).reshape(self.length, self.length)
        self.isInfinite = Infinite

        if Seed == 'random':
            self.Randomise()
        elif Seed == '5':
            self.Scenario5()
        elif Seed == 'glider':
            self.AddGlider()


    # Returns a grid with randomised nxn cells
    def Randomise(self): 
        self.grid = Num.random.choice(self.Values, self.length*self.length, p=[0.15, 0.85]).reshape(self.length, self.length) 

    # Returns a grid equal to the initial state in scenario 5 on the test brief
    def Scenario5(self): 
        self.grid[(self.length//2), (self.length//2)+1] = ON
        self.grid[(self.length//2),     self.length//2] = ON
        self.grid[(self.length//2), (self.length//2)-1] = ON

    def AddGlider(self):
        """adds a glider with top left cell at (i, j)"""
        glider = Num.array([[OFF, OFF, ON],  
                           [ON , OFF, ON],  
                           [OFF,  ON, ON]]) 
        self.grid[0:3, 0:3] = glider 

    # Returns true if we need to extend the board grid due to live cells at the edge
    def EdgeCase(self):
        EdgeCases = 0
        Top       = sum(self.grid[0,:])    
        Left      = sum(self.grid[:,0])
        Right     = sum(self.grid[-1,:])
        Bottom    = sum(self.grid[:,-1])

        EdgeCases = Top + Left + Right + Bottom    

        if self.isInfinite and EdgeCases != 0:
            return True
        else:
            return False

