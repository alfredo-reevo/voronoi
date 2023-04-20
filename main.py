import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy as sp
import random

# matplotlib init
plt.rcParams["font.family"] = "STIXGeneral"
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.size"] = 12

#* Simulation Variables
n = 5                   # Number of seeds

class point:

    def __init__(self, x, y, name):
        self.s = np.array[[x], [y]]
        self.name = name

def findMidpoint(p1, p2):
    mpX = (p1[0]+p2[0])/2
    mpY = (p1[1]+p2[1])/2
    midpoint = np.array([[mpX], [mpY]])
    #print(midpoint)
    return midpoint

def findGradient(p1, p2):
    grad = (p2[1]-p1[1])/(p2[0]-p1[0])
    normalGrad = -1/grad
    return normalGrad

def lineCalc(p1, p2):
    midpoint = findMidpoint(p1, p2)
    grad = findGradient(p1, p2)
    c = midpoint[1, 0] - (grad*midpoint[0, 0])
    x = np.arange(0, 11)
    y = (grad*x) + c
    ax.scatter(midpoint[0, 0], midpoint[1, 0], s=10, color="black")
    ax.annotate("MP(1, 2)", (midpoint[0, 0], midpoint[1, 0]))
    ax.plot(y, color="black", linestyle="dashed")

#* Plot settings
fig, ax = plt.subplots()
ax.set_ylim(0, 12)
ax.set_xlim(0, 12)
ax.set_aspect("equal")

xPoints = []
yPoints = []
seeds = np.array([[], []])
for i in range(0, n):
    xPoints.append(random.uniform(1, 10))
    yPoints.append(random.uniform(1, 10))
    seeds = np.append(seeds, [[xPoints[i]], [yPoints[i]]], axis=1)
    print(f"(x, y) = ({xPoints[i]}, {yPoints[i]})")

print(f"Coordinate Matrix: \n {seeds}")

#print(seeds)
#findGradient(seeds[:, 0], seeds[:, 1])

ax.scatter(xPoints, yPoints)
for i in range(0, len(xPoints)):
    ax.annotate(i+1, (xPoints[i], yPoints[i]), xycoords="data")


lineCalc(seeds[:, 0], seeds[:, 1])

plt.show()