# HydroGeoPy
Some Python code that may eventually be of some use to hydrogeologists

What works currently?

The simplehydro module contains functions based on Darcy's Law to calculate discharge, flow, hydraulic gradient, plug flow etc.

The helpers module contains functions to calculate travel time, distance travelled, velocity, average hydraulic conductivity values, decay constants, retardation, effective diffusion, one dimensional dispersion etc

The conversion module contains various unit conversions.

The one_d_analytical module implements the Donmenico equation for both concentrations and flux.

The one_d_numerical module implements one dimensional numerical solutions to the advection dispersion equation for both concentrations and flux assuming a concentration boundary condition of zero at an infinite distance and finite distance.  Numerical inversion in Laplace transform space is accomplished using the Stehfest algorithm.  The coefficients used in the numerical inversion are generated using the code in the inervsion module.

What's still to do?

More examples!
Implement a probailistic model framework based on monte carlo simulation.
Implement more analytical and numercial solutions.
Implement a consistent framework for storing and displaying results rather than ad-hoc calls to matplotlib.
Implement the Stehfest algorithm as an separate function.

Has it been validated?  Not really. However, one of the examples "exampleLinerVALIDATION" compares results with a published example. 
