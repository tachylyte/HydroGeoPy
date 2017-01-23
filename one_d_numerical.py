### Implementation of the numerical Stehfest inversion inspired by J Barker https://www.uni-leipzig.de/diffusion/presentations_DFII/pdf/DFII_Barker_Reduced.pdf

import inversion
import math

def finiteConc(t, v, De, R, deg, x, c0, L, N):
    ''' t is time (T), v is velocity (L/T), De is effective hydrodynamic dispersion (including diffusion) (L^2/T), 
    	R is retardation (-), lamda is first order decay constant (1/T), x is position along path (L),
    	C0 is source concentration (M/L^3), L is pathway length (L), n is effective porosity (-), N is input variable stehfestCoeff().
    	Return concentration (M/L^3) at position x'''
    Vs = inversion.stehfestCoeff(N)
    rt = math.log(2.0) / t
    Sum = 0
    for i in range(1, N+1):
        s = i * rt
        Sum = Sum + Vs[i - 1] * (c0 / s) * ((math.exp(((((v + (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * x)) + ((((v - (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * L))) - math.exp(((((v - (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * x)) + ((((v + (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * L)))) / (math.exp((((v - (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * L)) - math.exp((((v + (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * L))))
    return rt * Sum

def finiteFlux(t, v, De, R, deg, x, c0, L, n, N):
    ''' t is time (T), v is velocity (L/T), De is effective hydrodynamic dispersion (including diffusion) (L^2/T), 
    	R is retardation (-), lamda is first order decay constant (1/T), x is position along path (L),
    	C0 is source concentration (M/L^3), L is pathway length (L), n is effective porosity (-), N is input variable stehfestCoeff().
    	Return concentration (M/L^3) at position x'''
    Vs = inversion.stehfestCoeff(N)
    rt = math.log(2.0) / t
    Sum = 0
    for i in range(1, N+1):
        s = i * rt
        a1 = (v - (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)
        a2 = (v + (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)
        z1 = (v - (De * a2))
        z2 = (v - (De * a1))
        Sum = Sum + Vs[i - 1] * ((c0 * n) / s) * ((((z1 * math.exp((a2 * x) + (a1 * L))) - (z2 * math.exp((a1 * x) + (a2 * L)))) / (math.exp(a1 * L) - math.exp(a2 * L))))
    return rt * Sum

def infiniteConc(t, v, De, R, deg, x, c0, N):
    ''' t is time (T), v is velocity (L/T), De is effective hydrodynamic dispersion (including diffusion) (L^2/T), 
    	R is retardation (-), lamda is first order decay constant (1/T), x is position along path (L),
    	C0 is source concentration (M/L^3), n is effective porosity (-), N is input variable stehfestCoeff().
    	Return concentration (M/L^3) at position x'''
    Vs = inversion.stehfestCoeff(N)
    rt = math.log(2.0) / t
    Sum = 0
    for i in range(1, N+1):
        s = i * rt
        Sum = Sum + Vs[i - 1] * (c0 / s) * math.exp(((v - (v ** 2 + (4 * De * R * (s + deg))) ** 0.5) / (2 * De)) * x)
    return rt * Sum

def infiniteFlux(t, v, De, R, deg, x, c0, n, N):
    ''' t is time (T), v is velocity (L/T), De is effective hydrodynamic dispersion (including diffusion) (L^2/T), 
    	R is retardation (-), lamda is first order decay constant (1/T), x is position along path (L),
    	C0 is source concentration (M/L^3), n is effective porosity (-), N is input variable stehfestCoeff().
    	Return concentration (M/L^3) at position x'''
    Vs = inversion.stehfestCoeff(N)
    rt = math.log(2.0) / t
    Sum = 0
    for i in range(1, N+1):
        s = i * rt
        Sum = Sum + Vs[i - 1] * (((c0 * n) / s) * ((v - (De * ((v - ((v ** 2) + (4 * De * R * (s + deg))) ** 0.5) / (2 * De)))) * math.exp(((v - (v ** 2 + (4 * De * R * (s + deg))) ** (1 / 2)) / (2 * De)) * x)))
    return rt * Sum
