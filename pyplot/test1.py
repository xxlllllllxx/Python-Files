import matplotlib.pyplot as plt
import random as rnd


def math_calc(x, y):
    arr = []
    for i in range(x, y):
        arr += [i, i**2, i+2*i]
    return arr


fig = plt.figure()
plt.plot(math_calc(1, 100))
plt.ylabel('some numbers')
fig.savefig('pyplot/plot.png')
