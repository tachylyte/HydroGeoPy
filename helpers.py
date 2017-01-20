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

def retardation(###):
    #####
    return ###

def effectiveDiffusion(####):
    ######
    return De

def dilution(####):
    #######
    return ####
