# Useful helper functions
import conversion
import math

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

def decayConstant(time):
    '''Assume halflife (T) as input.
    Return first order decay rate in 1/T.'''
    return math.log(2) / time

def halfLife(decay):
    '''Assume decay rate in 1/T as input.
    Return half life (T).'''
    return math.log(2) / decay

def retardation(bulkD, n, Kd):
    '''Assume inputs bulk density (kg/l), effective porosity (-), partition coefficient Kd (l/kg).
    Return retardation factor.'''
    return 1 + ((bulkD / n) * Kd)

def effectiveDiff(Dw, tau):
    '''Assume free water diffusion coefficient Dw (m^2/s) and tortuosity tau (-) is greater than 1.
    Return effective diffusion coefficient De (m^2/s)'''
    return Dw / tau

def one_d_dispersion(L, v, Dw, tau, disp=0.1):
    '''Assume L is pathway length (m), dispersivity is assumed as 10% of pathway length in x-direction, 
    v is the average linear groundwater flow velocity (m/s), Dw is free water difussion coefficient (m^2/s),
    tau is tortuosity (greater than 1).  Disp is the fraction of path length
    used to calculate dispersivity.  The default which does not needs to be specified
    is 0.1 and for a negative velocity (advection against dispersion) disp is set at 0.
    Return hydrodynamic dispersion, D (m^2/s).'''
    if v < 0:
        alpha = 0
    else:
        alpha = L * disp
    D = (alpha * v) + effectiveDiff(Dw, tau)
    return D

def taylorDiffusion(n, poreThroat, v, Dw):
    Dtay = (n * poreThroat**2 * ((1.5 * v)**2))/(192*Dw)
    return Dtay
    
def one_d_dispTaylor(L, v, Dw, tau, Dtay, disp=0.1):
    '''Assume L is pathway length (m), dispersivity is assumed as 10% of pathway length in x-direction, 
    v is the average linear groundwater flow velocity (m/s), Dw is free water difussion coefficient (m^2/s),
    tau is tortuosity (greater than 1).  Disp is the fraction of path length
    used to calculate dispersivity.  The default which does not needs to be specified
    is 0.1 and for a negative velocity (advection against dispersion) disp is set at 0.
    Return hydrodynamic dispersion, D (m^2/s).'''
    if v < 0:
        alpha = 0
    else:
        alpha = L * disp
    D = (alpha * v) + effectiveDiff(Dw, tau)
    print('dispersivity = ' + str(alpha))
    return D
