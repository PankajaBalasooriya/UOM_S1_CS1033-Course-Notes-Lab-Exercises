class Cell:
    def __init__(self, i, j, north=False, east=False, south=False, west=False):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.visited = False
        self.i = i
        self.j = j


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
            cell = Cell(i, j, maze_boundaries[i][j][0], maze_boundaries[i][j][1], maze_boundaries[i][j][2],
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


def traverse():
    global Maze, stack, text

    cell = stack.top()

    # position = f"({cell.i}, {cell.j})"
    # print(position)

    cell.visited = True
    if (cell.i, cell.j) == (11, 13):
        text += f"Leaving at {printCoordinate((cell.i, cell.j))}"
        return

    if cell.north and not Maze[cell.i - 1][cell.j].visited:
        stack.push(Maze[cell.i - 1][cell.j])
        text += "North "
        traverse()
    elif cell.east and not Maze[cell.i][cell.j + 1].visited:
        stack.push(Maze[cell.i][cell.j + 1])
        text += "East "
        traverse()
    elif cell.south and not Maze[cell.i + 1][cell.j].visited:
        stack.push(Maze[cell.i + 1][cell.j])
        text += "South "
        traverse()
    elif cell.west and not Maze[cell.i][cell.j - 1].visited:
        stack.push(Maze[cell.i][cell.j - 1])
        text += "West "
        traverse()
    else:
        text += f"Stuck at ( {cell.i} , {cell.j} )"
        print(text)
        text = ""
        stack.pop()
        print(f"Back to ( {stack.top().i} , {stack.top().j} )")
        traverse()


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
    stack = Stack()
    text = ""
    position = ""
    print("Start at ( 2 , 0 )")
    stack.push(Maze[2][0])

    traverse()
    print(text)
