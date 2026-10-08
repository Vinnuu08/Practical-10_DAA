class DisjointSet:
    def __init__(self, vertices):
        # Initialize each vertex as its own parent with a rank of 0
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        # Find the root representative of the set with path compression
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            # Attach the smaller depth tree under the root of the deeper tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False  # They were already in the same set (would cause a cycle)


def kruskal_mst(vertices, edges):
    """
    Finds the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param vertices: List of vertices, e.g., [0, 1, 2, 3] or ['A', 'B', 'C']
    :param edges: List of tuples representing (weight, u, v)
    :return: A tuple containing (list of MST edges, total weight of MST)
    """
    # 1. Sort all edges in non-decreasing order of their weight
    sorted_edges = sorted(edges, key=lambda edge: edge[0])
    
    dsu = DisjointSet(vertices)
    mst = []
    total_weight = 0
    
    # Target number of edges in an MST is V - 1
    target_edges = len(vertices) - 1

    # 2. Iterate through sorted edges
    for weight, u, v in sorted_edges:
        # 3. If adding the edge doesn't form a cycle, include it
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
            # Optimization: Stop early if we have already found V-1 edges
            if len(mst) == target_edges:
                break
                
    return mst, total_weight


# --- Example Usage ---
if __name__ == "__main__":
    # Define vertices
    nodes = [0, 1, 2, 3, 4]
    
    # Define edges as (weight, source, destination)
    graph_edges = [
        (9, 0, 1),
        (5, 0, 2),
        (2, 1, 2),
        (7, 1, 3),
        (4, 2, 3),
        (3, 2, 4),
        (6, 3, 4)
    ]
    
    mst_edges, min_cost = kruskal_mst(nodes, graph_edges)
    
    print("Edges included in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == Weight: {weight}")
    print(f"Total Minimum Cost: {min_cost}")
