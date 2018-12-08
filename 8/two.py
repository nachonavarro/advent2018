from one import G

def size(node=0):
    metadata = G.node[node]['meta']
    total = 0
    if G.out_degree(node) == 0:
        total = sum(metadata)
    else:
        children = list(G.out_edges(node))
        for meta in metadata:
            if meta - 1 < len(children):
                total += size(children[meta - 1][1])
    return total

res = size()
print(res)