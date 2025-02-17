import numpy as np

class Laby:
    def __init__(self, a, b):
        # Initialize the maze dimensions a (rows), b (columns)
        self.a = a
        self.b = b
        self.laby = self.create_empty(a, b)
    
    @staticmethod
    def create_empty(a, b):
        """Creates an empty maze with walls"""
        empty = np.ones((2*a-1, 2*b-1))
        for i in range(a):
            for j in range(b):
                empty[2*i][2*j] = 2  # Cell
        for i in range(a-1):
            for j in range(b-1):
                empty[2*i+1][2*j+1] = 0  # Path
        return empty

    def add_mur(self, i1, j1, i2, j2):
        """Add a wall between two cells"""
        if i1 == i2 and abs(j1 - j2) == 1:
            self.laby[2*i1][j1 + j2] = 0
        if j1 == j2 and abs(i1 - i2) == 1:
            self.laby[i1 + i2][2*j1] = 0

    def remove_mur(self, i1, j1, i2, j2):
        """Remove a wall between two cells"""
        if i1 == i2 and abs(j1 - j2) == 1:
            self.laby[2*i1][j1 + j2] = 1
        if j1 == j2 and abs(i1 - i2) == 1:
            self.laby[i1 + i2][2*j1] = 1

    def display(self):
        """Display the maze in a readable format"""
        for i in range(len(self.laby[0])):
            print("#", end="")
        print("##")
        for row in self.laby:
            print("#", end="")
            for cell in row:
                if cell == 2:
                    print("*", end="")  # Cell
                elif cell == 1:
                    print(" ", end="")  # Path
                else:
                    print("H", end="")  # Wall
            print("#")
        for i in range(len(self.laby[0])):
            print("#", end="")
        print("##")

    def is_laby_valid(self):
        """Check if the maze meets the conditions for a valid maze"""
        if len(self.cellulesPossible(0, 0)) != (len(self.laby) + 1) * (len(self.laby[0]) + 1) / 4:
            print("NOT All cells are connected!")
            return False
        
        n = 0
        for row in self.laby:
            for cell in row:
                if cell == 1:
                    n += 1
        
        if n != (len(self.laby) + 1) * (len(self.laby[0]) + 1) / 4 - 1:
            print("NOT One possible way!")
            return False
        return True

    def cellulesPossible(self, i, j):
        """Check the adjacent cells"""
        # Placeholder for actual function
        return [(i+1, j), (i, j+1)]  # Example return value


# Example of usage
if __name__ == "__main__":
    # Create a 4x4 maze
    laby = Laby(4, 4)
    
    # Add a wall between two cells
    laby.add_mur(1, 1, 1, 2)
    laby.remove_mur(1, 1, 2, 1)

    # Display the maze
    laby.display()

    # Check if the maze is valid
    if laby.is_laby_valid():
        print("Maze is valid!")
    else:
        print("Maze is invalid!")
