import re, numpy

def get_info():
    parse = lambda line: [int(g) for g in re.match(r'#(.*) @ (.*),(.*): (.*)x(.*)', line).groups()]
    claims = [parse(claim) for claim in open('in.txt')]

    width  = max(x + width for _, x, _, width, _ in claims) + 1
    height = max(y + height for _, _, y, _, height in claims) + 1
    claim_matrix = numpy.zeros([height, width])
    for _, x, y, width, height in claims:
        claim_matrix[x:x + width, y:y + height] += 1

    return claim_matrix, claims

res = sum(1 for row in get_info()[0] for col in row if col > 1)
print(res)