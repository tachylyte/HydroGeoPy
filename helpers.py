# Useful helper functions

def travelTime(velocity, distance):
    '''Assume veolicty and distance provided.
    Return time of travel for distance'''
    time = distance / velocity
    return time

def distanceTravelled(velocity, time):
    '''Assume velocity and time provided.
    Return distance.'''
    distance = velocity * time
    return distance

def velocity(distance, time):
    '''Assume distance and time provided.
    Return velocity.'''
    velocity = distance / time
    return velocity

def aveVertK(*args):
    '''Accepts multiple layers.  Need a hydraulic conductivity (K) and thickness (L) for each.
    Specify all the K values before the L values e.g. if there are two layers the variables passed
    to the function will be K1, K2, L1, L2.
    Return the average vertical hydraulic conductivity.'''
    numberArgs = len(args)
    split = numberArgs // 2
    listK = args[:split]
    listL = args[split:]
    if len(listK) != len(listL):
        raise Exception('Unequal number of arguments')
    sumThickness = 0
    sumLdivK = 0
    for t in listL:
        sumThickness = sumThickness + t
    for i in range(len(listK)):
        sumLdivK += listL[i] / listK[i]
    aveVertK = sumThickness / sumLdivK
    return aveVertK

def aveHorizK(*args):
    '''Accepts multiple layers.  Need a hydraulic conductivity (K) and thickness (L) for each.
    Specify all the K values before the L values e.g. if there are two layers the variables passed
    to the function will be K1, K2, L1, L2.
    Return the average horizontal hydraulic conductivity.'''
    numberArgs = len(args)
    split = numberArgs // 2
    listK = args[:split]
    listL = args[split:]
    if len(listK) != len(listL):
        raise Exception('Unequal number of arguments')
    sumThickness = 0
    sumKL = 0
    for t in listL:
        sumThickness = sumThickness + t
    for i in range(len(listK)):
        sumKL += listL[i] * listK[i]
    aveHorizK = sumKL / sumThickness 
    return aveHorizK

def decayConstant(days):
    '''Assume halflife in days as input.
    Return first order decay rate in 1/s.'''
    return 1 / daysToSec(days)

def halfLife(decay):
    '''Assume decay rate in 1/s as input.
    Return half life in days'''
    return 1 / secsToDays(decay)

def retardation(bulkD, n, Kd):
    '''Assume inputs bulk density (kg/l), effective porosity (-), partition coefficient Kd (l/kg).
    Return retardation factor.'''
    return 1 + ((bulkD / n) * Kd)

def effectiveDiff(Dw, tau):
    '''Assume free water diffusion coefficient Dw (m^2/s) and tortuosity tau (-) is greater than 1.
    Return effective diffusion coefficient De (m^2/s)'''.
    return Dw / tau

def dilution(####):
    #######
    return ####
