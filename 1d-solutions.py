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

def finiteFlux(t, v, De, R, deg, x, c0, L, n, N):
    ''' t is time (T), v is velocity (L/T), De is effective diffusion coefficient (L^2/T), 
    	R is retardation (-), lamda is first order decay constant (1/T), x is position along path (L),
    	C0 is source concentration (M/L^3), L is pathway length (L), n is effective porosity (-).
    	Return concentration (M/L^3) at position x'''
    Vs = inversion.stehfestCoeff(N)
    # print(Vs)
    rt = math.log(2.0) / t
    Sum = 0
    for i in range(1, N+1):
        s = i * rt
        a1 = (v - (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)
        a2 = (v + (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)
        z1 = (v - (De * a2))
        z2 = (v - (De * a1))
        Sum = Sum + Vs[i - 1] * ((c0 * n) / s) * ((((z1 * math.exp((a2 * x) + (a1 * L))) - (z2 * math.exp((a1 * x) + (a2 * L)))) / (math.exp(a1 * L) - math.exp(a2 * L))))
        # print(Sum)
    return rt * Sum

#def finiteFluxabstracted(t, v, De, R, deg, x, c0, L, n)
  #  f = Vs[i - 1] * ((c0 * n) / s) * ((((z1 * math.exp((a2 * x) + (a1 * L))) - (z2 * math.exp((a1 * x) + (a2 * L)))) / (math.exp(a1 * L) - math.exp(a2 * L))))
    #return inversion.inverseTransform(f)    

flux = finiteFlux(t, v, De, R, deg, x, c0, L, n, 16)
print(flux, 'kg/s/m2')
print(flux * 1000000, 'mg/s/m2')
print((((flux * 1000000) * 60 * 60 * 24) / 1000), 'g/day/m2')
print('3.83e-1', ' final answer')
