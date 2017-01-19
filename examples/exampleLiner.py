# Calculation of vertical concentration profile and contaminantion mass flux through a two layer 
# mineral barrier with ponded contaminated water above the barrier and a higher K underlying unit.
# Concentrations are calculated using analytical and numerical solutions with boundary conditions
# assuming that zero-concentration is at infinity distance.  A numerical approach is also used to
# calculate the concentration profile taking into using a numerical solution which assumes the
# concentration in the higher K layer under the barrier is zero (a finite boundary condition).

# Import the necessary modules
import math              
import inversion
import simplehydro   
import helpers

# Liner geometry
K1= ####       #  K of liner layer 1 (m/s)
K2 = ####      #  K of liner layer 2 (m/s)
L1 = ####       # Thickness of liner layer 1
L2 = ####       # Thickness of liner layer 2

L =    # Total liner thickness (m)
K = helpers.aveVertK(K1, K2, L1, L2)  # average vertical hydraulic conductivity (m/s)

# Hydraulic gradient
h2 = ##### # Head above liner top (m) [depth of ponded water]
h1 = ##### # Head at base of liner (m) [is the high K layer underlying liner confined?]
i =    # Hydraulic gradient (-)

# Calculation of average liner groundwater flow velocity
q = simplehydro.darcy(K, i)   # Specific discharge (m/s)
n = 0.14             # Effective porosity (-)
v = 1.9e-6          # Average linear velocity (m/s)  

# Retardation
R =   helpers.retardation()   #1.93e1  

# Effective diffusion coefficient
De = 1.15e-7

# Biodegration
deg = 1.46499e-9   # First order degration coefficient

# Contaminant source concentration
c0 = conversion.kgPerM3(22)   # Convert kg/m^3 to g/m^3 (same as mg/l)

# Coefficient used by inversion module to calculate the Stehfest coeffcients for the numerical
# inversion of the numerical solutions in Laplace transform space
N = 16   # Values between 12 and 16 often give acceptable results for contaminant transport

# Fixed point at which to calculate contaminant concentration and mass flux
x = 0.6

# Time
t = conversion.daysToSecs(6.9) #convert days to seconds
# could try #  for t in range(secs(100)):


flux = finiteFlux(t, v, De, R, deg, x, c0, L, n, 16)
print(flux, 'kg/s/m2')
print(flux * 1000000, 'mg/s/m2')
print((((flux * 1000000) * 60 * 60 * 24) / 1000), 'g/day/m2')
print('3.83e-1', ' final answer')

dilututed concentration

plots
