import inversion
import math

t = 5961600 # s
v = 1.9e-6
De = 1.15e-7
R = 1.93e1
deg = 1.46499e-9
x = 0.6
c0 = 0.022
L = 0.6
n = 0.14
N = 16



flux = finiteFlux(t, v, De, R, deg, x, c0, L, n, 16)
print(flux, 'kg/s/m2')
print(flux * 1000000, 'mg/s/m2')
print((((flux * 1000000) * 60 * 60 * 24) / 1000), 'g/day/m2')
print('3.83e-1', ' final answer')
