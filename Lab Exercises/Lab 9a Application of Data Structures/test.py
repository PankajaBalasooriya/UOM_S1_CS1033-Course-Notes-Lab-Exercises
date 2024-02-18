def insert(self, data, bracketed):
    """
    Insert operators and operands into the binary tree.

    :param data: Operator or operand as a tuple. E.g.: ('OPERAND', 34), ('OPERATOR', ‘+’)
    :param bracketed: denote whether an operator is inside brackets or not. If the operator is inside brackets,
    we set bracketed as True.
    :return: self
    """

    # Include your code here

    global numberNode
    global BnewNode
    # checking if the value is operand
    if data[0] == "OPERAND":
        if BnewNode:
            numberNode = Node(data)
            BnewNode.right = numberNode
            self.right = BnewNode
            BnewNode = None
        else:
            numberNode = Node(data)
            self.right = numberNode
    else:
        # if it is a operator
        if bracketed:
            BnewNode = Node(data)
            BnewNode.left = numberNode
            # self.right = newNode
        else:
            newroot = Node(data)
            newroot.left = self
            return newroot

    return self