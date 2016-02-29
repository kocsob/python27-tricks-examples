import json


class Node(object):
    """Node class of Binary Tree"""

    def __init__(self, value, left=None, right=None):
        """Node initialization"""
        self.value = value
        self.left = left
        self.right = right

    def delete(self):
        """Delete node"""
        if self.left is not None and self.right is not None:
            parent_successor, successor = self.right.successor(self)
            parent_successor.left = successor.right
            successor.left = self.left
            successor.right = self.right
            self.replace(successor)
        elif self.left is not None and self.right is None:
            self.replace(self.left)
        elif self.right is not None and self.left is None:
            self.replace(self.right)
        return None

    def successor(self, parent):
        """Find successor"""
        if self.left is not None:
            return self.left.successor(self)
        return parent, self

    def replace(self, other):
        """Node replace"""
        self.__init__(other.value, other.left, other.right)

    @property
    def __dict__(self):
        """Change dict property"""
        dictionary = {'value': self.value}
        if self.left:
            dictionary['left'] = self.left
        if self.right:
            dictionary['right'] = self.right

        return dictionary


class BinaryTree(object):
    """Binary tree class"""

    def __init__(self):
        """Binary tree initialization"""
        self.root = None

    def insert(self, value):
        """Public insert function"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Protected insert function for recursive call"""
        if value < node.value:
            if node.left is not None:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def find(self, value):
        """Public find function"""
        if self.root is None:
            return None

        return self._find(self.root, value)

    def _find(self, node, value):
        """Protected find function for recursive call"""
        if node.value == value:
            return node
        elif node.value > value and node.left is not None:
            return self._find(node.left, value)
        elif node.value < value and node.right is not None:
            return self._find(node.right, value)
        else:
            return None

    def min(self):
        """Minimum function"""
        if self.root is None:
            return None

        node = self.root
        while node.left is not None:
            node = node.left

        return node.value

    def max(self):
        """Maximum function"""
        if self.root is None:
            return None

        node = self.root
        while node.right is not None:
            node = node.right

        return node.value

    def size(self):
        """Public size function"""
        return self._size(self.root)

    def _size(self, node):
        """Protected size function for recursive call"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def inorder(self):
        """Public inorder traversal function"""
        return self._inorder(self.root)

    def _inorder(self, node):
        """Protected inorder traversal function for recursive call"""
        if node is None:
            return ""

        text = self._inorder(node.left)
        text += str(node.value) + " "
        text += self._inorder(node.right)
        return text

    def delete(self, value):
        """Delete node function"""
        node = self.find(value)
        if node is not None:
            node.delete()

    def serialize(self):
        """Serialize Binary Tree to JSON string"""
        return json.dumps(self.root, default=lambda obj: obj.__dict__)

    def deserialize(self, string):
        """Deserialize Binary Tree from JSON string"""
        self.root = json.loads(string, object_hook=lambda kwargs: Node(**kwargs))

    def __str__(self):
        """Override default string function"""
        return json.dumps(self.root, default=lambda obj: obj.__dict__, sort_keys=True, indent=2)


if __name__ == "__main__":
    btree = BinaryTree()
    btree.insert(30)
    btree.insert(20)
    btree.insert(35)
    btree.insert(19)
    btree.insert(21)
    btree.insert(32)
    btree.insert(36)
    btree.insert(33)
    print btree.inorder()
    print 'minimum:', btree.min()
    print 'maximum:', btree.max()
    print 'size:', btree.size()
    btree.delete(30)
    print btree.inorder()
    btree.deserialize(btree.serialize())
    print btree
