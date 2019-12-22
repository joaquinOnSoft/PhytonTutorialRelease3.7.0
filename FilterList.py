import math
import random

raw = []
for i in range(10):
    if random.randint(0, 1) == 0:
        raw.append(random.random())
    else:
        raw.append(float('NaN'))

print("Raw data: ", raw)

filtered = []
for i in raw:
    if not math.isnan(i):
        filtered.append(i)

print("Filtered data: ", filtered)

print("Original size: ", len(raw), "\tFiltered size:", len(filtered))
