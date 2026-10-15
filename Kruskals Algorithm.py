class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


def kruskal(num_vertices, edges):
    # Step 1: Sort all edges by weight
    edges.sort(key=lambda item: item[2])

    dsu = DisjointSet(num_vertices)
    mst = []
    total_weight = 0

    # Step 2: Greedily pick the smallest edge that doesn't form a cycle
    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight


if __name__ == "__main__":
    print("--- Kruskal's Algorithm MST Finder ---")
    
    # 1. Take number of vertices and edges from user
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    edges = []
    print(f"\nEnter {num_edges} edges in the format: source destination weight")
    print("Example: 0 1 10")
    
    # 2. Loop to take each edge's details
    for i in range(num_edges):
        u, v, weight = map(int, input(f"Edge {i+1}: ").split())
        edges.append((u, v, weight))

    # 3. Calculate MST
    mst_edges, min_cost = kruskal(num_vertices, edges)

    # 4. Display results
    print("\n" + "="*35)
    print("Edges in the Minimum Spanning Tree:")
    print("="*35)
    for u, v, w in mst_edges:
        print(f"  {u} -- {v}  (Weight: {w})")
    
    print(f"\nTotal Minimum Cost: {min_cost}")
