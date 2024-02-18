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

        # Making variables accessible across the method calls
        global numberNode
        global BracketNode
        # Checking if the value is an operand
        if data[0] == "OPERAND":
            if BracketNode:
                # If the operator is inside brackets, attaching the operand to the right of the BracketNode
                numberNode = Node(data)
                BracketNode.right = numberNode
                self.right = BracketNode
                BracketNode = None
            else:
                # If the operator is not inside brackets, attaching the operand to the right of the current node
                numberNode = Node(data)
                self.right = numberNode
        else:
            # If it is an operator
            if bracketed:
                # If the operator is inside brackets, creating a new node for the operator and attaching it to the left
                # of the previously encountered operand (numberNode)
                BracketNode = Node(data)
                BracketNode.left = numberNode
            else:
                # If the operator is not inside brackets, creating a new root node for the tree with the current operator.
                # Attaching the current tree as the left child of the new root node.
                newroot = Node(data)
                newroot.left = self
                return newroot
        # Returning the updated tree
        return self

    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''

        # Include your code here
        def evaluate_tree(root):
            '''
            Recursive helper function to evaluate the expression stored in the binary tree.
            :param root: The current root node of the binary tree.
            :return: Evaluated value of the expression or operand at the current root node.
            '''
            if root.data[0] == "OPERATOR":
                # If the current node is an operator, evaluating its left and right subtrees
                opr = root.data[1]
                n1 = evaluate_tree(root.left)
                n2 = evaluate_tree(root.right)

                # Perform the operation and updating the root node with the result as a new operand
                root.data = ("OPERAND", do_operator(n1, opr, n2))
                # Set the left and right children to None, to remove the subtree
                root.left, root.right = None, None
                # Return the evaluated value for the current root node
                return root.data
            else:
                # If the current node is an operand, return its value
                return root.data

        # DO the evaluation process from the root of the tree and return the final result
        return evaluate_tree(self)[1]


def do_operator(number1, operator, number2):
    '''
    Perform the specified arithmetic operation on the operands.

    :param number1: The first operand as a tuple ('OPERAND', value).
    :param operator: The arithmetic operator (+, -, *, ^).
    :param number2: The second operand as a tuple ('OPERAND', value).
    :return: The result of the arithmetic operation.
    '''
    # Check the operator and perform the corresponding arithmetic operation
    match operator:
        case "+":
            return number1[1] + number2[1]
        case "-":
            return number1[1] - number2[1]
        case "*":
            return number1[1] * number2[1]
        case "^":
            return number1[1] ** number2[1]


numberNode = None
BracketNode = None
