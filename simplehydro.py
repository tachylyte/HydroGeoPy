# Functions for performing simple hydrogeological calculations

def discharge(K, i, A, *args, **kwargs):
    Q = K * i * A
    return Q

def gradient(Q, K, A):
    i = Q / (K * A)
    return i

def area(Q, K, i):
    A = Q / (K * i)
    return A

def specificDischarge1(Q, A):
    q = Q / A
    return q

def specificDischarge2(K, i):
    q = k * i
    return q

def velocity1(q, n):
    v = q / n
    return v

def velocity2(K, i, n):
    v = velocity1(K, i) / n
    return v
    
def darcy(**kw):
    '''Assume keyword inputs are a subset of K, i, A, v and n.
    Calculate missing variable based on the inputs given.
    Returns the value.'''
    discharge_set = set("KiA")
    gradient_set = set("QKA")
    area_set = set("QKi")
    specificDischarge1_set = set("QA")
    specificDischarge2_set = set("Ki")
    velocity1_set = set("qn")
    velocity2_set = set("Kin")
    if set(kw.keys()) == discharge_set:
        Q = discharge(**kw)
        return Q
    if set(kw.keys()) == gradient_set:
        i = gradient(**kw)
        return i
    if set(kw.keys()) == area_set:
        A = area(**kw)
        return A
    if set(kw.keys()) == specificDischarge1_set:
        q = specificDischarge1(**kw)
        return q
    if set(kw.keys()) == specificDischarge2_set:
        q = specificDischarge2(**kw)
        return q
    if set(kw.keys()) == velocity1_set:
        v = velocity1(**kw)
        return v
    if set(kw.keys()) == velocity2_set:
        v = velocity2(**kw)
        return v        
    else:
        raise Exception('Invalid inputs')   

def Darcy(**kw):
    '''Assume keyword inputs are a subset of K, i, A, v and n.
    Calculate missing variable based on the inputs given.
    Prints the value and says what it has calculated.'''
    discharge_set = set("KiA")
    gradient_set = set("QKA")
    area_set = set("QKi")
    specificDischarge1_set = set("QA")
    specificDischarge2_set = set("Ki")
    velocity1_set = set("qn")
    velocity2_set = set("Kin")
    if set(kw.keys()) == discharge_set:
        Q = discharge(**kw)
        return print('Discharge, Q =', Q)
    if set(kw.keys()) == gradient_set:
        i = gradient(**kw)
        return print('Hydraulic gradient, i =', i)
    if set(kw.keys()) == area_set:
        A = area(**kw)
        return print('Area, A =', A)
    if set(kw.keys()) == specificDischarge1_set:
        q = specificDischarge1(**kw)
        return print('Specific discharge, \q =', q)
    if set(kw.keys()) == specificDischarge2_set:
        q = specificDischarge2(**kw)
        return print('Specific discharge, q =', q)
    if set(kw.keys()) == velocity1_set:
        v = velocity1(**kw)
        return print('Average linear geoundwater flow velocity, v =', v)
    if set(kw.keys()) == velocity2_set:
        v = velocity2(**kw)
        return print('Average linear groundwater flow velocity, v =', v)        
    else:
        raise Exception('Invalid inputs')   
    

