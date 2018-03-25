# For sparse graph, use list of vertex for dense graph, use adjacency matrix for quick lookup.
# Adjacency matrix - quick lookup, more space (v^2)
# List of vertex, may be less space, but lokup for path between vertex can be O(v^2). To optimize use hash of hashset.
# Another way to represent graph is list of edges.
# List<Edge>   v1---v2   Edge: Vertex1, Vertex2
# For weighted graph, in adjacency matrix, fill with weights instead of 0/1.
#
#
# Traverse the graph
def dfs(visited_map, v):
    if v in visited_map:
        return

    print v.val
    visited_map[v] = 1
    for n in v.neighbors:
        dfs(visited_map, n)

# Visit all neighbor first. Then their children. Ideal for shorted path
def bfs(v):
    queue = [v]
    visited = {}

    while len(queue) > 0:
        node = queue.pop(0)
        if node not in visited:
            print node.val
            visited[node] = 1
            for c in node.neighbors:
                child.append(c)


def bfs_get_path(v, dst):
    queue = [v]
    path[v] = None
    visited = {}

    while len(queue) > 0:
        node = queue.pop(0)
        if node not in visited:
            print node.val
            visited[node] = 1
            for c in node.neighbors:
                if c not in path: # If node is already enqueued, but not visited yet, we don't want to add it again in path agin
                    path[c] = node
                    child.append(c)
    return path

def get_path(path, dst):
    p = path[dst]
    out_path = [dst]
    while p != None:
        out_path.append(p)
        p = path[p]
    out_path = out_path[::-1]


# Clone a graph. Based on dfs
def clone(v, clone_map):
    if v in clone_map:
        return clone_map[v]

    v_clone = Node(v)
    clone_map[v] = v_clone

    for n in v.neighbors:
        v_clone.append(clone(n))

    return v_clone


def get_neighbors(matrix, i, j):
    # Return top, bottom, left, right, diagnonal cells

def dfs(matrix, i, j, visited):
    visited[j][i] = 1
    neighbors = get_neighbors(matrix,i,j)
    for n in neighbors:
        visited[n.col][n.row] = 1
        dfs(matrix, col, row)

# Find islands.
# 0 - water, 1 - land
def count_islands(matrix, rows, columns):
    visited = [[1 for i in range(columns)] for j in range(rows)]
    count = 0
    for i in columns:
        for j in rows:
            if (matrix[j][i] == 1) and (visited[j][i] == 0):
                dfs(matrix, i, j, visited)
                count += 1

    return count


# Given list of words, find all valid transformations
# cat bat mat hat car bar...
# Input: cat -> bar
# Output: cat -> bat,bat->bar
#         cat->car, bar->bar
# Brute force:   complexity = V^2*m
# For w1 in dict:
#       For w2 in dict:
#               if word_diff(w1, w2) ==1:
#                       w1, w2 are neighbors
#
# Approach 1: For each word, replace each with 25 chars of alphabet, if found in input map of words, they are neighbors O(26m*V)
# Approach 2: Replace each char in each word with *, add other words matching the pattern in the same bucket. 
# At the end, different buckets will contain neighbors O(V*m) with extra space


# Topological sorting
# If directed graph (A,B) process A before B
# Keep 2 maps, processed and unprocessed.
# DFS: Visited each node, put in unprocessed. If each of my outbound connections are processed, then mark it processed.
#                                             If some outbound connections are not processed, then dfs them.
#                                              O (v^2*delta)
# Approach 2: Visit all nodes
#             When finished processing, go back to its parent. O(V*delta)
# Lot of applications - builds, package installation dependencies, Thread parallelize/sequential, Map reduce, Data pipeline
#


# Given list of sorted words, sorted using another alphabet order, output the ordered alphabet
# Topological sort

#
# Djikstra's algorithm
# Find shortest path between src and dst in a weighted directed graph
# 1. Initialize ditance vector
#               for src = 0, for all other nodes = infinity
#     Add all nodes to unprocessed set
# 2. Pick next closest neighbor a
# 3. Update weights of a's neighbors such that distance(src, neighbor) = min(distance(src,a)+edge(a,neighbor), distance(src,neighbor))
# 4. Repeat 2. Remove A from unprocessed
#    Time complexity: O(V^2 + V*delta) = O(V^2+E)
# For optimizing above, for step 2, Use minheap. O(V * delta*logV) = O(ElogV)
# Undirected graph - count delta twice - inbound, outbound

#





