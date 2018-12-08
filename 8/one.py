tree, lengths = [int(x) for x in open('in.txt').read().split()], {}

def node_length(pos=0):
    children, metadata = tree[pos:pos + 2]
    length = 2
    if children:
        for child in range(children):
            length += node_length(pos + length)
    lengths[pos + length] = metadata
    return length + metadata

node_length()
res = sum(sum(tree[start:start + end]) for start, end in lengths.items())
print(res)