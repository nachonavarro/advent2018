import networkx as nx

tree, G = [int(x) for x in open('in.txt').read().split()], nx.DiGraph()

def node_length(pos=0):
    children, metadata = tree[pos:pos + 2]
    length = 2
    if children:
        for child in range(children):
            G.add_edge(pos, pos + length)
            length += node_length(pos + length)
    G.add_node(pos, meta=tree[pos + length:pos + length + metadata])
    return length + metadata

node_length()
res = sum(sum(meta) for meta in nx.get_node_attributes(G, 'meta').values())
print(res)