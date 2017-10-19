# Set of functions for generating monte carlo distributions

from random import *
import math

def Single(a, i):
    samples = []
    for i in range (1, i+1):
        samples.append(a)
    return samples

def Uniform(a, b, i):
    samples = []
    for i in range (1, i+1):
        samples.append(uniform(a, b))
    return samples

def Loguniform(a, b, i):
    samples = []
    for i in range (1, i+1):
        samples.append(math.log(uniform(a, b)))
    samples = [math.exp(x) for x in samples]
    return samples

def Triangular(low, high, mode, i):
    samples = []
    for i in range (1, i+1):
        samples.append(triangular(low, high, mode))
    return samples

def Normal(mu, sigma, i):
    samples = []
    for i in range (1, i+1):
        samples.append(normalvariate(mu, sigma))
    return samples

def Lognormal(mu, sigma, i):
    samples = []
    for i in range (1, i+1):
        samples.append(lognormvariate(mu, sigma))
    return samples
