import math

def domenicoConc(t, v, De, R, deg, x, c0):
    ''' t is time (T), v is velocity (L/T), De is effective hydrodynamic dispersion (including diffusion) (L^2/T), 
    R is retardation (-), deg is first order decay constant (1/T), x is position along path (L),
    c0 is source concentration (M/L^3), n is effective porosity (-), N is input variable stehfestCoeff().
    Return concentration (M/L^3) at position x'''
    a = math.sqrt(1 + ((4 * deg * R * De) / (v**2)))
    b = 1 / (2 * math.sqrt((De * t) / R))
    c = b * ((x - ((v * t) / R)) * a)
    d = math.erfc(c)
    e = (v * x) / (2 * De)
    f = math.exp(e * (1 - a))
    g = math.erfc(b * ((x + ((v * t) / R) * a)))
    h = math.exp(e * (1 + a))
    i = c0  * ((f * d) + (h * g)) / 2
    return i

def domenicoFlux(t, v, De, R, deg, x, c0, n):
    ''' t is time (T), v is velocity (L/T), De is effective hydrodynamic dispersion (including diffusion) (L^2/T), 
    R is retardation (-), deg is first order decay constant (1/T), x is position along path (L),
    c0 is source concentration (M/L^3), n is effective porosity (-).
    Return concentration (M/L^3) at position x'''
    a = math.sqrt(1 + ((4 * deg * R * De) / (v**2)))
    b = 1 / (2 * math.sqrt((De * t) / R))
    c = (v * x) / (2 * De)
    d = 0.5 * (1 + a) * math.exp(c * (1 - a)) * math.erfc((b * (x - ((v * t)/R)*a)))
    e = 0.5 * (1 - a) * math.exp(c * (1 + a)) * math.erfc((b * (x + ((v * t)/R)*a)))
    f = 1 / v
    g = math.sqrt((R*De)/(math.pi*t))                                                          
    h = math.exp(c*(1-a))
    i = math.sqrt(R/(4*De*t))
    j = (v*t)/R
    k = x - (j*a)
    l = math.exp(-1*(i*(k))**2)
    m = f * g * h * l
    o = ((n * v * c0) / 2) * (d + e + m)                                                  
    return o
