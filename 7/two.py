import networkx

G = networkx.DiGraph()
G.add_edges_from((line[5], line[36]) for line in open('in.txt'))

res, workers, max_workers = 0, {}, 5
while len(G):
    roots = [node for node, degree in G.in_degree() if degree == 0]
    for root in roots:
        if len(workers) < max_workers and root not in workers:
            workers[root] = ord(root) - 4
    for worker in list(workers):
        workers[worker] -= 1
        if workers[worker] == 0:
            G.remove_node(worker)
            del workers[worker]
    res += 1

print(res)