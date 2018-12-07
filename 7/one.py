import re, networkx as nx

G = nx.DiGraph()
G.add_edges_from((line[5], line[36]) for line in open('in.txt'))

res = ''
while len(G):
    root = min(node for node, degree in G.in_degree() if degree == 0)
    res += root
    G.remove_node(root)

print(res)