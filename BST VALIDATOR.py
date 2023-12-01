class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Solution 1
    # def add_child(self, data):
    #     if data == self.data:
    #         return
    #     if data < self.data:
    #         if self.left:
    #             return self.left.add_child(data)
    #         else:
    #             self.left = BinarySearchTree(data)
    #     else:
    #         if self.right:
    #             return self.right.add_child(data)
    #         else:
    #             self.right = BinarySearchTree(data)

    def tree_root(self, root):
        def in_order_traversal(root, elements):
            if root is None:
                return
            in_order_traversal(root.left, elements)
            elements.append(root.data)
            in_order_traversal(root.right, elements)

        elements = []
        in_order_traversal(root, elements)
        print(elements)
        return elements == sorted(elements)


# Solution 1
# def tree_builder(datas):
#     root = BinarySearchTree(datas[0])
#     for i in range(1, len(datas)):
#         root.add_child(datas[i])
#     return root
#
# data = []
#
# while True:
#     element = int(input("Enter the Element or 00 to Exit: "))
#     data.append(element)
#     if element == 00:
#         data.pop()
#         break
# solution = BinaryChecker()
# print(solution.tree_root(tree_builder(data)))

# Solution 2:
# #Root
# root = BinarySearchTree(10)
# #Left
# root.left = BinarySearchTree(8)
# root.left.left = BinarySearchTree(7)
# root.left.right = BinarySearchTree(9)
#
# #Right
# root.right = BinarySearchTree(9)
# root.right.left = BinarySearchTree(11)
#
# print(root.tree_root(root))
