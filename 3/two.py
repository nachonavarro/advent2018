import numpy
from one import get_info

claim_matrix, claims = get_info()
for res, x, y, width, height in claims:
    if (claim_matrix[x:x + width, y:y + height] == numpy.ones([width, height])).all():
        break

print(res)