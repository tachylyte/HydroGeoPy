# Simple test of probabilistic modelling
# Calculates time to break through assuming plug flow

from simplehydro import *
from monte_carlo import *
from conversion import *
import matplotlib.pyplot as plt

# Probabilistic
I = 100001                      # Number of iterations
K = Loguniform(1e-8, 1e-7, I)   # Input distrubution for K
x = 10                          # Distance, x (m)
n = 0.3                         # Effective porosity, n (-)
H = 1                           # Head where x=0 (m)
h = 0                           # Head where x=x (m)

i = gradient2(H, h, x)

results = []
for iteration in range(I):
    results.append(velocity2(K[iteration], i, n))
results = [round(secsToDays(x/v), 2) for v in results]    # Calculate breakthroughs
#print(results)

toPlot = [K, results]
for plot in toPlot:
    # the histogram of the data
    n, bins, patches = plt.hist(results, 50, normed=1, facecolor='green', alpha=0.75)
    # add a 'best fit' line
    #l = plt.plot(bins, results, 'r--', linewidth=1)
    #plt.xlabel('Breakthrough (days)')
    plt.title(plot)
    plt.ylabel('Probability density')
    plt.axis([0, max(results), 0, 200/I])
    plt.grid(True)
    plt.show()
