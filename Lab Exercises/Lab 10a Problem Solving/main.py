class Cell:
    def __init__(self, north=False, east=False, south=False, west=False):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.visited = False


class Stack:
    def __init__(self, size=196):
        """
        :param size: size of the stack
        """
        self.buffer = list()
        self.size = size
        self.length = 0

    def push(self, item):
        """
        Adding or inserting the item to the top of the stack
        :param item: Item to be added to the stack
        :return: status value indicating the success or the failure of the operation
        """
        if self.length < self.size:
            self.buffer.insert(0, item)
            self.length += 1
            return 0
        return 1

    def pop(self):
        """
        Deleting or removing the item at the top of the stack
        :return: item if the operation is successful, else return None
        """
        item = None
        if self.length > 0:
            item = self.buffer[0]
            self.buffer.pop(0)
            self.length -= 1
        return item

    def empty(self):
        """
        Checking if the stack is empty
        :return: boolean isempty or not
        """
        if self.length == 0:
            return True
        return False

    def length(self):
        """
        Obtaining the length of the stack
        :return: length of the stack
        """
        return len(self.buffer)

    def top(self):
        """
        :return: the reference to the element at the top of the stack, without removing from the stack
        """
        return self.buffer[0]


def maze(maze_boundaries):
    """
    Creating the maze using a matrix and with cell objects
    :return:
    """
    # maze = [[[] for j in range(14)] for i in range(14)]
    maze = [[] for i in range(14)]

    for i in range(14):
        for j in range(14):
            cell = Cell(maze_boundaries[i][j][0], maze_boundaries[i][j][1], maze_boundaries[i][j][2],
                        maze_boundaries[i][j][3])
            maze[i].append(cell)
    return maze


def printCoordinate(coordinate):
    """
    conver tuple format of the coordinate to printing format
    :param coordinate: coordinate tuple
    :return: string of the printing form
    """
    return f"( {coordinate[0]} , {coordinate[1]} )"


def traverse(coordinates):
    i = coordinates[0]
    j = coordinates[1]

    global Maze, stack, text

    if (i, j) == (11, 13):
        text += f"Leaving at {printCoordinate(coordinates)}"
        return

    cell = Maze[i][j]

    cell.visited = True
    stack.push(cell)

    if cell.north and not Maze[i - 1][j].visited:
        north_cell = Maze[i - 1][j]
        text += "North "
        traverse((i - 1, j))
    elif cell.east and not Maze[i][j + 1].visited:
        east_cell = Maze[i][j + 1]
        text += "East "
        traverse((i, j + 1))
    elif cell.south and not Maze[i + 1][j].visited:
        south_cell = Maze[i + 1][j]
        text += "South "
        traverse((i + 1, j))
    elif cell.west and not Maze[i][j - 1].visited:
        west_cell = Maze[i][j - 1]
        text += "West "
        traverse((i, j - 1))
    else:
        if cell.north and Maze[i - 1][j].visited:
            pass
        elif cell.east and Maze[i][j + 1].visited:
            pass
        elif cell.south and Maze[i + 1][j].visited:
            pass
        elif cell.west and Maze[i][j - 1].visited:
            stack.pop()

            text += f"Stuck at ( {i} , {j} )"






if __name__ == '__main__':
    boundaries = [
        [[False, True, True, False], [False, True, False, True], [False, True, True, True], [False, False, False, True],
         [False, True, True, False], [False, True, False, True], [False, False, True, True],
         [False, True, False, False], [False, True, True, True], [False, True, False, True],
         [False, False, False, True], [False, True, True, False], [False, True, False, True],
         [False, False, True, True]],
        [[True, False, True, False], [False, True, False, False], [True, True, False, True],
         [False, False, False, True], [True, False, True, False], [False, True, False, False],
         [True, True, False, True], [False, True, True, True], [True, False, True, True], [False, True, False, False],
         [False, True, False, True], [True, True, False, True], [False, False, False, True],
         [True, False, True, False]],
        [[True, True, True, False], [False, True, True, True], [False, False, False, True], [False, True, True, False],
         [True, False, False, True], [False, True, True, False], [False, False, False, True],
         [True, False, True, False], [True, True, False, False], [False, True, False, True], [False, True, False, True],
         [False, False, True, True], [False, True, True, False], [True, False, True, True]],
        [[True, False, True, False], [True, False, True, False], [False, True, True, False], [True, True, True, True],
         [False, True, False, True], [True, False, False, True], [False, True, False, False], [True, True, False, True],
         [False, False, False, True], [False, True, True, False], [False, True, False, True],
         [True, False, False, True], [True, False, True, False], [True, False, True, False]],
        [[True, False, True, False], [True, False, True, False], [True, False, True, False], [True, False, True, False],
         [False, True, True, False], [False, True, False, True], [False, True, False, True], [False, False, True, True],
         [False, True, True, False], [True, False, False, True], [False, True, True, False], [False, True, False, True],
         [True, False, False, True], [True, False, True, False]],
        [[True, False, True, False], [True, False, True, False], [True, False, False, False],
         [True, False, True, False], [True, False, True, False], [False, True, True, False],
         [False, False, False, True], [True, False, True, False], [True, False, True, False],
         [False, True, True, False], [True, False, True, True], [False, True, True, False], [False, False, True, True],
         [True, False, False, False]],
        [[True, False, False, False], [True, True, True, False], [False, False, True, True], [True, False, True, False],
         [True, False, True, False], [True, False, True, False], [False, True, True, False], [True, True, False, True],
         [True, False, False, True], [True, False, True, False], [True, False, True, False], [True, False, True, False],
         [True, False, True, False], [False, False, True, False]],
        [[False, False, True, False], [True, False, True, False], [True, False, True, False],
         [True, False, True, False], [True, False, True, False], [True, False, True, False], [True, True, True, False],
         [False, False, False, True], [False, False, True, False], [True, False, False, False],
         [True, True, True, False], [True, False, False, True], [True, False, True, False], [True, False, True, False]],
        [[True, False, True, False], [True, False, False, False], [True, True, True, False], [True, False, False, True],
         [True, False, True, False], [True, True, False, False], [True, False, False, True], [False, True, True, False],
         [True, False, False, True], [False, False, True, False], [True, False, True, False],
         [False, True, True, False], [True, True, False, True], [True, False, True, True]],
        [[True, True, True, False], [False, True, False, True], [True, True, False, True], [False, False, False, True],
         [True, True, False, False], [False, True, False, True], [False, False, True, True], [True, True, False, False],
         [False, True, False, True], [True, True, False, True], [True, False, True, True], [True, False, True, False],
         [False, False, True, False], [True, False, True, False]],
        [[True, False, False, False], [False, False, True, False], [False, True, True, False],
         [False, True, False, True], [False, True, False, True], [False, False, True, True], [True, True, True, False],
         [False, False, True, True], [False, True, True, False], [False, True, False, True], [True, False, False, True],
         [True, False, True, False], [True, False, True, False], [True, False, True, False]],
        [[False, True, True, False], [True, False, True, True], [True, False, True, False], [False, True, True, False],
         [False, False, True, True], [True, True, False, False], [True, False, False, True], [True, False, True, False],
         [True, True, False, False], [False, True, False, True], [False, False, True, True], [True, False, True, False],
         [True, True, False, False], [True, True, False, True]],
        [[True, False, True, False], [True, True, False, False], [True, False, False, True], [True, False, True, False],
         [True, True, False, False], [False, True, True, True], [False, False, False, True],
         [True, False, False, False], [False, True, True, False], [False, True, False, True],
         [True, False, False, True], [True, True, False, False], [False, False, False, True],
         [False, False, True, False]],
        [[True, True, False, False], [False, True, False, True], [False, True, False, True], [True, True, False, True],
         [False, False, False, True], [True, True, False, False], [False, True, False, True],
         [False, True, False, True], [True, True, False, True], [False, True, False, True], [False, True, False, True],
         [False, True, False, True], [False, True, False, True], [True, False, False, True]]]

    Maze = maze(boundaries)

    print("Start at ( 2 , 0 )")

    stack = Stack()
    text = ""

    traverse((2, 0))
    print(text)
