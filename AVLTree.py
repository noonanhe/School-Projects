import random as r
import queue

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.height == other.height

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result
            
    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """
        Inserts the node with the given value
        :param node: root of the tree
        :param value: value to insert
        :return: the root of the subtree the value is inserted at
        """
        if node is None:
            node = Node(value)
            self.size +=1
            if self.root is None:
                self.root = node
            return node
        elif value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        self.update_height(node)
        node = self.rebalance(node)
        return node

    def remove(self, node, value):
        """
        Removes the node with the given value
        :param node: root of subtree node will be removed from
        :param value: value to be removed
        :return: the root of the subtree
        """
        """For an empty tree"""
        if self.size == 0:
            return None

        if not node:
            return node
        elif value < node.value:
            node.left = self.remove(node.left, value)
        elif value > node.value:
            node.right = self.remove(node.right, value)
        else:
            if node.left is None:
                """Special case for root"""
                if node is self.root:
                    self.root.value = node.right.value
                    node.right = self.remove(node.right, node.right.value)
                    self.update_height(self.root)
                    self.size -= 1
                temp = node.right
                node = None
                self.size -= 1
                return temp
            elif node.right is None:
                """Special case for root"""
                if node is self.root:
                    self.root.value = node.left.value
                    node.left = self.remove(node.left, node.left.value)
                    self.update_height(self.root)
                    self.size -= 1
                temp = node.left
                node = None
                self.size -= 1
                return temp
            temp = self.max(node.left)
            node.value = temp.value
            node.left = self.remove(node.left, temp.value)

        self.update_height(node)
        node = self.rebalance(node)
        return node

    def search(self, node, value):
        """
        Searches for the given value in the tree
        :param value:value to search for
        :param node:root of given tree
        :return: node with the given value, or the potential
            parent node if the value isn't found
        """
        while node is not None:
            if value == node.value:
                return node
            elif value < node.value:
                if node.left is None:
                    return node
                node = node.left
            else:
                if node.right is None:
                    return node
                node = node.right

    def inorder(self, node):
        """
        Traverses the tree inorder
        :param node: root node
        :return: generator object of the traversed tree
        """
        if node is not None:
            #if node.left is not None:
            yield from self.inorder(node.left)
            yield node
            #if node.right is not None:
            yield from self.inorder(node.right)

    def preorder(self, node):
        """
        Visits the parent node first traversal
        :param node: root of the tree
        :return: generator object of the traversed tree
        """
        if node is not None:

            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def postorder(self, node):
        """
        Traverses the tree visiting parent node last
        :param node:root of tree
        :return:generator object of the traversed tree
        """
        if node is not None:

            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node

    def breadth_first(self, node):
        """
        Traverses the tree level by lebe
        :param node:root of the tree
        :return: nodes in breadth first order
        """
        q = [node]
        while q:
            n = q.pop(0)
            if n is not None:
                yield n
                q.append(n.left)
                q.append(n.right)

    def depth(self, value):
        """
        returns the depth of the node with the given value
        :param value:value of the node
        :return:depth of the node with the given value
        """
        if self.size == 0:
            return -1
        node = self.root
        depth = 0
        while node is not None and node.value != value:
            if node.value < value:
                node = node.right
            elif node.value > value:
                node = node.left
            depth += 1
        if node is None:
            return -1
        else:
            return depth

    def height(self, node):
        """
        returns the height of the tree
        :param node: root of the tree
        :return: height of the tree
        """
        if node is None:
            return -1
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        return 1 + max(l_height, r_height)


    def update_height(self, node):
        """
        Updates the height of a given node
        :param node: node to update height of
        """
        l_height = -1
        if node.left is not None:
            l_height = node.left.height
        r_height = -1
        if node.right is not None:
            r_height = node.right.height
        node.height = 1 + max(l_height, r_height)

    def min(self, node):
        """
        finds the minimum of the tree
        :param node: root of the tree
        :return: minimum of tree
        """
        if self.size == 0:
            return None
        if node.left is None or node is None:
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        """
        finds the maximum of the tree
        :param node: root of the tree
        :return: max of the tree
        """
        if self.size == 0:
            return None
        if node.right is None or node is None:
            return node
        else:
            return self.max(node.right)

    def get_size(self):
        """
        Gets size of the tree
        :return:tree size
        """
        return self.size


    def get_balance(self, node):
        """
        Gets balance factor of a node
        :param node: node to get balance factor of
        :return: balance factor
        """
        if node.left is None:
            l_height = -1
        else:
            self.update_height(node.left)
            l_height = node.left.height
        if node.right is None:
            r_height = -1
        else:
            self.update_height(node.right)
            r_height = node.right.height
        return l_height - r_height

    def left_rotate(self, root):
        """
        Performs a left rotation
        :param root: root of subtree
        :return: root of the new subtree
        """
        right = root.right
        left = right.left

        if root is self.root:
            self.root = right

        right.left = root
        right.parent = root.parent
        if right.parent is not None:
            if right.parent.value < right.value:
                right.parent.right = right
            else:
                right.parent.left = right
        root.parent = right

        root.right = left
        if left is not None:
            left.parent = root

        self.update_height(root)
        self.update_height(right)
        if left is not None:
            self.update_height(left)
        return right

    def right_rotate(self, root):
        """
        Performs a right rotation
        :param root: root of subtree
        :return: root of new subtree
        """
        left = root.left
        right = left.right

        #checking if we need to reassign the root node
        if root is self.root:
            self.root = left

        left.right = root
        left.parent = root.parent
        if left.parent is not None:
            if left.parent.value > left.value:
                left.parent.left = left
            else:
                left.parent.right = left
        root.parent = left

        root.left = right
        if right is not None:
            right.parent = root

        self.update_height(root)
        self.update_height(left)
        if right is not None:
            self.update_height(right)

        return left

    def rebalance(self, node):
        """
        Reblances the tree
        :param node: root of subtree
        :return: root of new subtree
        """
        self.update_height(node)
        if self.get_balance(node) == -2:
            if self.get_balance(node.right) == 1:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        return node


def sum_update(root, total):
    """
    Sums and replaces the values with the sum of the values
    greater than or equal to them
    :param root: root of a BST
    :param total: total of the nodes
    :return: total
    """
    if root is None:
        return total

    total = sum_update(root.right, total)
    total = total + root.value
    root.value = total
    if root.parent is not None and root.parent.left == root:
        swap_children(root.parent)
    total = sum_update(root.left, total)
    if root.left is None or root.left.value > root.value:
        temp = root.left
        root.left = root.right
        root.right = temp

    return total


def swap_children(parent):
    """
    Swaps the children of a given node
    :param parent: node of switch children of
    """
    temp = parent.right
    parent.right = parent.left
    parent.left = temp


