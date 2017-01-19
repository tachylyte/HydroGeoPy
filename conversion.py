# Useful unit conversions

def days(s):
    '''Assume s is time in seconds and a positive integer or float.
    Return time in days'''
    days = s / (60 * 60 * 24) 
    return days

def secs(d):
    '''Assume d is time in days and a positive integer or float.
    Return time in seconds'''
    secs = (60 * 60 * 24) * d
    return secs

def year(d):
    '''Assume d is time in days and a positive integer or float.
    Return time in years'''
    year = 365.25 / d
    return year

def mPerS(mPerD):
    '''Assume mPerD is a positive integer or float.
    Return mPerS'''
    mPerS = days(mPerD)
    return mPerS

def mPerD(mPerS):
    '''Assume mPerS is a positive integer or float.
    Return mPerD'''
    mPerD = secs(mPerS)
    return mPerD
