# Prefix search
# restaurants : {"PIZZA HUT", "PIEOLOGY", "OPA", "PASTA HOUSE", "PIZZA PLACE", ...} where N entries of max M chars each
# Query: PIZZA  where Q is length of query string
# Results: {"PIZZA HUT", "PIZZA PLACE"}
# Brute Force: For each input, compare with query string O(NQ + PM) - PM for result string copies..but generally O(NQ)
# Approach2 : Sorting and Binary Search : O(NMLOGN) setup cost for sorting. Binary search O(QLOGN + PM)  Q * LOG N 
# because once we get the bucket in binary search, we have to compare Q chars
# Approach3: For O(1) Create hash of all possible prefixes of N entries and values of
# restaurant names. Now search is O(1). Setup cost is O(NM) - number of prefix for each string is M so N*M
# Time complexity is O(Q + PM)
# Space complexity: O(N^2M) each row in hash can have all N entries, so # of prefixes = NM * Max each row of prefix = NM*N - huge
# Lets go with Approach 2 and try to improve on setup cost.
# Build a prefix tree or Trie. 
#                       Root
#               P               O
#           I   A               P
#       Z   E   S               A*
#      Z    O   T
#     A     L   A
#    H      O   H
#
#
# Setup cost : O(NM)
# Time complexity: O(Q + PM)  First Q compares to get to the prefix of query, 
# then remaining nodes in branches below need to be visited - atmost P results of ~M length in that branch
# Space complexity: O(NM)
#
#
class TrieNode(self):
    def __init__(self):
        self.child_char_map = {}
        self.is_word_end = False

def buildTrie(restaurants):
    root = Trienode()
    for name in restaurants:
        insertTrie(root, name)

        return root

def insertTrie(root, name):
    node = root
    for c in name.spit():
        if c not in name.child_char_map:
            name.child_char_map[c] = TrieNode()
        node = node.child_char_map[c]

    node.isWord = True

# Above can be done using tail recursion - and all tail recursion can be done using loop iteratively.
# Tail recursion means no branching, only path being called.
