# Calculation of vertical concentration profile and contaminantion mass flux through a two layer 
# mineral barrier with ponded contaminated water above the barrier and a higher K underlying unit.
# Concentrations are calculated using analytical and numerical solutions with boundary conditions
# assuming that zero-concentration is at infinity distance.  A numerical approach is also used to
# calculate the concentration profile taking into using a numerical solution which assumes the
# concentration in the higher K layer under the barrier is zero (a finite boundary condition).

# Import the necessary modules
import math
import pylab
import inversion
import conversion
import simplehydro   
import helpers
import one_d_numerical
import one_d_analytical

# Liner geometry
K1= 1e-8       #  K of liner layer 1 (m/s)
K2 = 1e-7      #  K of liner layer 2 (m/s)
L1 = 0.3       # Thickness of liner layer 1
L2 = 0.3       # Thickness of liner layer 2

L = L1 + L2 # Total liner thickness (m)
K = helpers.aveVertK(K1, K2, L1, L2)  # average vertical hydraulic conductivity (m/s)

# Hydraulic gradient
H = 1.6 # Head above liner top (m) [depth of ponded water]
h = 0 # Head at base of liner (m) [is the high K layer underlying liner confined?]
i =  (H - h) / L  # Hydraulic gradient (-)

# Calculation of average liner groundwater flow velocity
q = K * i    # Specific discharge (m/s)
n = 0.14             # Effective porosity (-)
v = q / n          # Average linear velocity (m/s)  

# Retardation
bulkD =  2.02  # Bulk density (kg/l or 1000kg/m^3)
Kd =   1.265       # l/kg
R = 1 + ((bulkD / n) * Kd)  #1.93e1   # Retardation  

# Effective hydrodynamic dispersion coefficient
Dw = 1.96e-9  # Free water diffusion coefficient (m^2/s)
tau = 5    # Tortuosity (-)
De = helpers.one_d_dispersion(L, v, Dw, tau)

# Biodegration
Half_life = 5.48e3 # days
Half_life =  conversion.daysToSecs(Half_life)   ####
deg =  helpers.decayConstant(Half_life)  #1.46499e-9   # First order degration coefficient

# Contaminant source concentration
c0 = conversion.kgPerM3(22)   # Convert kg/m^3 to g/m^3 (same as mg/l)

# Coefficient used by inversion module to calculate the Stehfest coeffcients for the numerical
# inversion of the numerical solutions in Laplace transform space
N = 16   # Values between 12 and 16 often give acceptable results for contaminant transport

# Fixed point for breakthrough curve
x = 0.45

# Time for fixed concentration profile
days = 90
t = conversion.daysToSecs(days) #convert days to seconds
# could try #  for t in range(secs(100)):

# Concentration profile calculations
xAxis, concFinite, concInfinite, fluxFinite, fluxInfinite = [], [], [], [], []
i = 0.01
while i <= L:
    xAxis.append(i)
    plugConc = simplehydro.plugFlow(t, v, R, i, c0)
    concPlug.append(plugConc*1000)
    analConc = one_d_analytical.domenicoConc(t, v, De, R, deg, i, c0)
    concAnal.append(analConc*1000)
    conc1 = one_d_numerical.finiteConc(t, v, De, R, deg, i, c0, L, N) 
    concFinite.append(conc1*1000)
    conc2 = (one_d_numerical.infiniteConc(t, v, De, R, deg, i, c0, N)) 
    concInfinite.append(conc2*1000)
    plugFlux = plugConc * q * 60 *60 * 24 * 1000 * 1
    fluxPlug.append(plugFlux)
    flux1 = one_d_numerical.finiteFlux(t, v, De, R, deg, i, c0, L, n, N)
    fluxFinite.append((((flux1 * 1000000) * 60 * 60 * 24) / 1000))
    flux2 = one_d_numerical.infiniteFlux(t, v, De, R, deg, i, c0, n, N)
    fluxInfinite.append((((flux2 * 1000000) * 60 * 60 * 24) / 1000))
    i += 0.01

pylab.figure(1)
pylab.plot(xAxis, concFinite)
pylab.plot(xAxis, concInfinite)
pylab.plot(xAxis, concPlug)
pylab.plot(xAxis, concAnal)
title1 = 'Concentration profile at ' + str(days) + ' days'
pylab.title(title1)
pylab.figure(2)
pylab.plot(xAxis, fluxFinite)
title2 = 'Flux profile at ' + str(days) + ' days'
pylab.title(title2)
pylab.plot(xAxis, fluxInfinite)
pylab.plot(xAxis, fluxPlug)
#pylab.show()

# Breakthrough profile calculations
zAxis, zconcPlug, zconcAnal, zconcFinite, zconcInfinite, zfluxPlug, zfluxFinite, zfluxInfinite = [0], [0], [0], [0], [0], [0], [0], [0]
z = 1
maxTime = 600
while z <= maxTime:
    zAxis.append(z)
    zplugConc = simplehydro.plugFlow(conversion.daysToSecs(z), v, R, x, c0)
    zconcPlug.append(zplugConc*1000)
    zanalConc = one_d_analytical.domenicoConc(conversion.daysToSecs(z), v, De, R, deg, x, c0)
    zconcAnal.append(zanalConc*1000)
    zconc1 = one_d_numerical.finiteConc(conversion.daysToSecs(z), v, De, R, deg, x, c0, L, N) 
    zconcFinite.append(zconc1*1000)
    zconc2 = (one_d_numerical.infiniteConc(conversion.daysToSecs(z), v, De, R, deg, x, c0, N)) 
    zconcInfinite.append(zconc2*1000)
    zplugFlux = zplugConc * q * 60 *60 * 24 * 1000 * 1
    zfluxPlug.append(zplugFlux)
    zflux1 = one_d_numerical.finiteFlux(conversion.daysToSecs(z), v, De, R, deg, x, c0, L, n, N)
    zfluxFinite.append((((zflux1 * 1000000) * 60 * 60 * 24) / 1000))
    zflux2 = one_d_numerical.infiniteFlux(conversion.daysToSecs(z), v, De, R, deg, x, c0, n, N)
    zfluxInfinite.append((((zflux2 * 1000000) * 60 * 60 * 24) / 1000))
    z += 1

pylab.figure(3)
pylab.plot(zAxis, zconcFinite)
pylab.plot(zAxis, zconcInfinite)
pylab.plot(zAxis, zconcPlug)
pylab.plot(zAxis, zconcAnal)
title3 = 'Concentration breakthrough at ' + str(x) + 'm'
pylab.title(title3)
pylab.figure(4)
pylab.plot(zAxis, zfluxFinite)
title4 = 'Flux breakthrough at ' + str(x) + 'm'
pylab.title(title4)
pylab.plot(zAxis, zfluxInfinite)
pylab.plot(zAxis, zfluxPlug)
pylab.show()




