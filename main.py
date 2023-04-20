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

class seed:

    def __init__(self, x, y, name):
        self.s = np.array([[x], [y]])
        print(self.s)
        self.name = name

    def findMidpoint(self, partnerSeed):
        mpX = (self.s[0, 0]+partnerSeed[0, 0])/2
        mpY = (self.s[1, 0]+partnerSeed[1, 0])/2
        midpoint = np.array([[mpX], [mpY]])
        #print(midpoint)
        return midpoint

    def findGradient(self, partnerSeed):
        grad = (partnerSeed[1, 0]-self.s[1, 0])/(partnerSeed[0, 0]-self.s[0, 0])
        normalGrad = -1/grad
        return normalGrad

    def lineCalc(self, partnerSeed, pSeedName):
        midpoint = self.findMidpoint(partnerSeed)
        grad = self.findGradient(partnerSeed)
        c = midpoint[1, 0] - (grad*midpoint[0, 0])
        x = np.arange(0, 22)
        y = (grad*x) + c
        ax.scatter(midpoint[0, 0], midpoint[1, 0], s=10, color="black")
        ax.annotate(f"MP({self.name}, {pSeedName})", (midpoint[0, 0], midpoint[1, 0]), alpha=0.5)
        ax.plot(y, color="black", linestyle="dashed")

#* Plot settings
fig, ax = plt.subplots()
ax.set_ylim(0, 22)
ax.set_xlim(0, 22)
ax.set_aspect("equal")

xPoints = []
yPoints = []
def createSeeds(n):
    seeds = np.array([])
    for i in range(0, n):
        x = random.uniform(1, 20)
        y = random.uniform(1, 20)
        seeds = np.append(seeds, seed(x, y, f"{i+1}"))
    return seeds
        
seeds = createSeeds(n)
print(seeds)


for i in range(0, len(xPoints)):
    ax.annotate(i+1, (xPoints[i], yPoints[i]), xycoords="data")



plt.show()
