import heapq

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = [None]

    def add_child(self, child):
        if self.children[0] == None:
            self.children[0] = child
        else:
            self.children.append(child)

def diameter(root):
    if root == None:
        return 0
    heights = []
    for c in root.children:
        heights.append(-1 * height(c))

    heapq.heapify(heights)
    max_height = 0
    max_height2 = 0
    if len(heights):
        max_height = -1 * heapq.heappop(heights)
    if len(heights):
        max_height2 = -1 * heapq.heappop(heights)


    diameters = []
    for c in root.children:
        diameters.append(-1 * diameter(c))
    heapq.heapify(diameters)
    max_diameter = 0
    if len(diameters):
        max_diameter = -1 * heapq.heappop(diameters)

    return max(1+max_height+max_height2, max_diameter)


def height(node):
    if node == None:
        return 0

    h = []
    for c in node.children:
        h.append(-1 * height(c))

    heapq.heapify(h)
    max_height = 0
    if len(h):
        max_height = -1 * heapq.heappop(h)
    return 1 + max_height


if __name__ == "__main__":
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    root.add_child(Node(3))
    root.add_child(Node(4))
    root.children[1].add_child(Node(11))
    root.children[1].children[0].add_child(Node(21))
    root.children[1].children[0].children[0].add_child(Node(31))
    root.children[2].add_child(Node(22))
    root.children[2].children[0].add_child(Node(32))
    root.children[2].children[0].children[0].add_child(Node(42))

    print diameter(root)
