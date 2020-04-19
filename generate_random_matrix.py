#naive method to generate the 4X4 matrix
import copy
import random

def shuffle(x, freq):
    y = copy.deepcopy(x);
    for i in range(0,freq):
        idx = int(random.uniform(0, len(x)));
        val = y.pop(idx);
        y.append(val);
    z = copy.deepcopy(y);
    return z
f=10
num=[1,2,3,4]
for i in range(0, 4):
    Y = shuffle(num, f)
    print(Y)
