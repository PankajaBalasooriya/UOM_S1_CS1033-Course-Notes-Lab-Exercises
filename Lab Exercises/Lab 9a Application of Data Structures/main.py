class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        '''
        Print the output depending on the evaluated value.
        If the 0 <= value <= 999 the value is printed.
        If the value < 0, UNDERFLOW is printed.
        If the value > 999, OVERFLOW is printed.

        :return: None
        '''
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)

    #####################################################################
    ######### Your task is to implement the following methods. ##########
    #####################################################################

    def insert(self, data, bracketed):
        '''
        Insert operators and operands into the binary tree.

        :param data: Operator or operand as a tuple. E.g.: ('OPERAND', 34), ('OPERATOR', ‘+’)
        :param bracketed: denote whether an operator is inside brackets or not. If the operator is inside brackets,
        we set bracketed as True.
        :return: self
        '''

        # Include your code here
        global numberNode
        global BracketNode
        # checking if the value is operand
        if data[0] == "OPERAND":
            if BracketNode:
                numberNode = Node(data)
                BracketNode.right = numberNode
                self.right = BracketNode
                BracketNode = None
            else:
                numberNode = Node(data)
                self.right = numberNode
        else:
            # if it is a operator
            if bracketed:
                BracketNode = Node(data)
                BracketNode.left = numberNode
                # self.right = newNode
            else:
                newroot = Node(data)
                newroot.left = self
                return newroot
        return self

    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''

        # Include your code here
        def calculate_tree_sum(root):
            if root.data[0] == "OPERATOR":
                opr = root.data[1]
                n1 = calculate_tree_sum(root.left)
                n2 = calculate_tree_sum(root.right)
                root.data = ("OPERAND", do_operator(n1, opr, n2))
                root.left, root.right = None, None
                return root.data
            else:
                return root.data

        return calculate_tree_sum(self)[1]


def do_operator(number1, operator, number2):
    if operator == "+":
        return number1[1] + number2[1]
    if operator == "-":
        return number1[1] - number2[1]
    if operator == "*":
        return number1[1] * number2[1]
    if operator == "^":
        return number1[1] ** number2[1]


numberNode = None
BracketNode = None

if __name__ == '__main__':

    # TestCase 1
    root = Node(('OPERAND', 1))
    root = root.insert(('OPERATOR', '+'), False)
    root = root.insert(('OPERAND', 2), False)
    root = root.insert(('OPERATOR', '*'), False)
    root = root.insert(('OPERAND', 3), False)
    root = root.insert(('OPERATOR', '+'), False)
    root = root.insert(('OPERAND', 3), False)
    root = root.insert(('OPERATOR', '^'), False)
    root = root.insert(('OPERAND', 2), False)


    '''
    # TestCase 2
    root = Node(('OPERAND', 1))
    root = root.insert(('OPERATOR', '+'), False)
    root = root.insert(('OPERAND', 2), False)
    root = root.insert(('OPERATOR', '*'), True)
    root = root.insert(('OPERAND', 3), False)
    root = root.insert(('OPERATOR', '+'), False)
    root = root.insert(('OPERAND', 3), False)
    root = root.insert(('OPERATOR', '^'), False)
    root = root.insert(('OPERAND', 2), False)
    '''
    '''
    root = Node(('OPERAND', -15))
    root = root.insert(('OPERATOR', '-'), False)
    root = root.insert(('OPERAND', 99), False)
    root = root.insert(('OPERATOR', '*'), True)
    root = root.insert(('OPERAND', 10), False)
    '''

    root.get_output()
