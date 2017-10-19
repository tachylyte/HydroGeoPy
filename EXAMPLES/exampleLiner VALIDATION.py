# Calculation of vertical concentration profile and contaminantion mass flux through a one layer 
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

L = 1 # Total liner thickness (m)
K = 8.5e-11  # average vertical hydraulic conductivity (m/s)

# Hydraulic gradient
H = 5 # Head above liner top (m) [depth of ponded water]
h = 6 # Head at base of liner (m) [is the high K layer underlying liner confined?]
i =  (H - h) / L  # Hydraulic gradient (-)
print('i = ' + str(i))

# Calculation of average liner groundwater flow velocity
q = K * i    # Specific discharge (m/s)
print('q = ' + str(q))
n = 0.162             # Effective porosity (-)
v = q / n          # Average linear velocity (m/s)
print('v = ' + str(v))

# Retardation
bulkD =  1.75  # Bulk density (kg/l or 1000kg/m^3)
Kd =   1       # l/kg
R = 1 + ((bulkD / n) * Kd)  #1.93e1   # Retardation  
print('R = ' + str(R))

# Effective hydrodynamic dispersion coefficient
Dw = 2.00e-9  # Free water diffusion coefficient (m^2/s)
tau = 2.33476    # Tortuosity (-)
poreThroat = 1e-5   # Pore throat radius (m) used to calculate taylor diffusion
Dtay = helpers.taylorDiffusion(n, poreThroat, v, Dw)
print('Dtay = ' + str(Dtay))
De = helpers.one_d_dispTaylor(L, v, Dw, tau, Dtay)
#De = helpers.effectiveDiff(Dw, tau)
print('De = ' + str(De))

# Biodegration
Half_life = 5000 # days
Half_life =  conversion.daysToSecs(Half_life)   
deg =  helpers.decayConstant(Half_life)   # First order degration coefficient
print('lamda = ' + str(deg))

# Contaminant source concentration
c0 = 1000 # mg/l
c0 = conversion.kgPerM3(c0)   # Convert  g/m^3 (same as mg/l) to kg/m^3

# Coefficient used by inversion module to calculate the Stehfest coeffcients for the numerical
# inversion of the numerical solutions in Laplace transform space
N = 12   # Values between 12 and 16 often give acceptable results for contaminant transport

# Fixed point for breakthrough curve
x = 1

# Time for fixed concentration profile
days = 1e7 # days
t = days * (60 * 60 * 24) #secs

# Concentration profile calculations
xAxis, concPlug, concAnal, concFinite, concInfinite, fluxPlug, fluxFinite, fluxInfinite, fluxAnal = [], [], [], [], [], [], [], [], []
i = 0.000000001
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
    plugFlux = plugConc * abs(q) * 1000 * 1
    fluxPlug.append(plugFlux)
    flux1 = one_d_numerical.finiteFlux(t, v, De, R, deg, i, c0, L, n, N)
    fluxFinite.append(flux1/1e6) 
    flux2 = one_d_numerical.infiniteFlux(t, v, De, R, deg, i, c0, n, N)
    fluxInfinite.append(flux2/1e6) 
    flux3 = one_d_analytical.domenicoFlux(t, v, De, R, deg, i, c0, n)
    fluxAnal.append(flux3/1e6)
    i += 0.0001

pylab.figure(1)
pylab.subplot(211)
pylab.plot(xAxis, concFinite, label='Numerical solution (finite boundary condition)')
pylab.plot(xAxis, concInfinite, label='Numerical solution (infinite boundary condition)')
pylab.plot(xAxis, concAnal, label='Analytical solution (infinite boundary condition)')
#pylab.plot(xAxis, concPlug, label='Plug flow')
ta = int(days / (365.25))
title1 = 'Concentration profile at ' + str(ta) + ' years'
pylab.title(title1)
pylab.xlabel('Distance (m)')
pylab.ylabel('Concentration (mg/l)')
pylab.legend(loc = 'best', prop={'size':8})

pylab.subplot(212)
pylab.plot(xAxis, fluxFinite, label='Numerical solution (finite boundary condition)')
title2 = 'Flux profile at ' + str(ta) + ' years'
pylab.title(title2)
pylab.plot(xAxis, fluxInfinite, label='Numerical solution (infinite boundary condition)')
pylab.plot(xAxis, fluxAnal, label='Analytical solution (infinite boundary condition)')
#pylab.plot(xAxis, fluxPlug, label='Plug flow')
pylab.xlabel('Distance (m)')
pylab.ylabel('Flux (mg/s/m2)')
pylab.legend(loc = 'best', prop={'size':8})

# Breakthrough curve calculations
zAxis, zconcPlug, zconcAnal, zconcFinite, zconcInfinite, zfluxPlug, zfluxFinite, zfluxInfinite, zfluxAnal = [0], [0], [0], [0], [0], [0], [0], [0], [0]
z = 5    # days
maxTime = 900000  # days
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
    zplugFlux = zplugConc * abs(q) * 1
    zfluxPlug.append(zplugFlux)
    zflux1 = one_d_numerical.finiteFlux(conversion.daysToSecs(z), v, De, R, deg, x, c0, L, n, N)
    zfluxFinite.append(zflux1)
    zflux2 = one_d_numerical.infiniteFlux(conversion.daysToSecs(z), v, De, R, deg, x, c0, n, N)
    zfluxInfinite.append(zflux2)
    zflux3 = one_d_analytical.domenicoFlux(conversion.daysToSecs(z), v, De, R, deg, x, c0, n)
    zfluxAnal.append(zflux3)
    z += 60

pylab.figure(2)
pylab.subplot(211)
pylab.plot(zAxis, zconcFinite, label='Numerical solution (finite boundary condition)')
pylab.plot(zAxis, zconcInfinite, label='Numerical solution (infinite boundary condition)')
pylab.plot(zAxis, zconcAnal, label='Analytical solution (infinite boundary condition)')
#pylab.plot(zAxis, zconcPlug, label='Plug flow')
title3 = 'Concentration breakthrough at ' + str(x) + 'm'
pylab.title(title3)
pylab.xscale('log')
pylab.xlabel('Time (days)')
pylab.ylabel('Concentration (mg/l)')
pylab.legend(loc = 'best', prop={'size':8})

pylab.subplot(212)
pylab.plot(zAxis, zfluxFinite, label='Numerical solution (finite boundary condition)')
title4 = 'Flux breakthrough at ' + str(x) + 'm'
pylab.title(title4)
pylab.plot(zAxis, zfluxInfinite, label='Numerical solution (infinite boundary condition)')
pylab.plot(zAxis, zfluxAnal, label='Analytical solution (infinite boundary condition)')
#pylab.plot(zAxis, zfluxPlug, label='Plug flow')
pylab.xlabel('Time (days)')
pylab.ylabel('Flux (mg/s/m2)')
pylab.xscale('log')
pylab.legend(loc = 'best', prop={'size':8})

# Print results to facilitate validation against p81 of "Contaminant fluxes from hydraulic containment landfills"
testTimes = []
numericalResults = []
analyticalResults = []
for i in range(6):
    testTimes.append(10**(i-2))
for j in testTimes:
    ni = one_d_numerical.infiniteConc(conversion.daysToSecs(conversion.yearToDay(j)), v, De, R, deg, L, c0, N)
    numericalResults.append(ni*1e6)
    ai = one_d_analytical.domenicoConc(conversion.daysToSecs(conversion.yearToDay(j)), v, De, R, deg, L, c0)
    analyticalResults.append(ai*1e6)

headers = ['Time(years)', 'Numerical solution', 'Analytical solution']
print('\nCONCENTRATION in mg/l\n', headers[0], ' ', headers[1], '  ', headers[2]) 
for k in range(len(testTimes)):
    results = '\t\t%.3e\t\t%.3e' % (numericalResults[k], analyticalResults[k])
    print(str(testTimes[k]), results)

numericalFluxResults = []
analyticalFluxResults = []
for l in testTimes:
    f1 = one_d_numerical.infiniteFlux(conversion.daysToSecs(conversion.yearToDay(l)), v, De, R, deg, x, c0, n, N)
    numericalFluxResults.append(f1)
    f2 = one_d_analytical.domenicoFlux(conversion.daysToSecs(conversion.yearToDay(l)), v, De, R, deg, x, c0, n)
    analyticalFluxResults.append(f2)

print('\nCONTAMINANT MASS FLUX in kg/s/m2\n', headers[0], ' ', headers[1], '  ', headers[2]) 
for m in range(len(testTimes)):
    resultsflux = '\t\t%.3e\t\t%.3e' % (numericalFluxResults[m], analyticalFluxResults[m])
    print(str(testTimes[m]), resultsflux)

pylab.show()




