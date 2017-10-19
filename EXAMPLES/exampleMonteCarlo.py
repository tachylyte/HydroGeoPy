# Simple test of probabilistic modelling
# Calculates time to break through assuming plug flow

from simplehydro import *
from monte_carlo import *
from conversion import *
import matplotlib.pyplot as plt

x = 10      # Distance, x (m)
n = 0.3     # Effective porosity, n (-)
K = 1e-7    # Hydraulic conductivity, K (m/s)
H = 1       # Head where x=0 (m)
h = 0       # Head where x=x (m)
i = gradient2(H, h, x)

# Deterministic
v = velocity2(K, i, n)
Breakthrough = x / v
print('Deterministic breakthrough in ' + str(round(secsToDays(Breakthrough), 2)) + ' days')

# Probabilistic
I = 100001                    # Number of iterations
pK = Normal(1e-7, 1e-8, I)  # Input distrubution for K

results = []
for iteration in range(I):
    results.append(velocity2(pK[iteration], i, n))
results = [round(secsToDays(x/v), 2) for v in results]    # Calculate breakthroughs
#print(results)

# the histogram of the data
n, bins, patches = plt.hist(results, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
#l = plt.plot(bins, results, 'r--', linewidth=1)

plt.xlabel('Breakthrough (days)')
plt.ylabel('Probability density')
plt.axis([0, max(results), 0, 200/I])
plt.grid(True)

plt.show()
