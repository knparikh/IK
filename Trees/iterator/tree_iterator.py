# Implement tree iterator
# O(1) time , O(h) memory
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())
    return deserialize()

class Iterator(object):
    def __init__(self, root):
        self.stack = []
        temp = root
        while temp:
            self.stack.append(temp)
            temp = temp.left


    def next(self):
        next_elem = self.stack.pop()
        temp = next_elem.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return next_elem

    def hasNext(self):
        return self.stack


_size = int(raw_input());
_str = raw_input()
root = createTree(_str);
itr = Iterator(root)
while itr.hasNext():
    print itr.next().val
