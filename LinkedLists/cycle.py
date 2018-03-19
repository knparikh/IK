# Check if LL has a cycle
# Brute force have a visited flag for each node, and mark to True as you traverse the LL
# Another brute force - keep hashset of memory reference
# Take 2 pointers, p1 and p2, advance p1 by 1 node, p2 by 2 nodes. If p2 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextp = None


def IsCycle(head):
    slow = head
    fast = head

    if fast == None:
        return False

    while (fast.nextp != None):
        fast = fast.nextp.nextp
        slow = slow.nextp

        if fast == slow:
            return True


    return False


def FindCycleStart(head):
    slow = head
    fast = head

    if fast == None:
        return None

    while (fast.nextp != None):
        fast = fast.nextp.nextp
        slow = slow.nextp

        if fast == slow:
            break


    if fast != None:
        p1 = head
        p2 = fast

        while (p1 != p2):
            p1 = p1.nextp
            p2 = p2.nextp

        return p1

    return None
