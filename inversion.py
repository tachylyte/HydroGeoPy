#Module for carrying out a numerical inversion of Laplace transforms.  
#There are functions to generate Stehfest coefficients and to implement the Stehfest inversion method

N = 16

def stehfestCoeff(N):    
    ''' Assume that N is an integer and N == 0
        Normally, the optimum value of N is determined as a result of a numerical experiment. As a reference, however, the range of 6 ≤ N ≤ 18 covers the most common values of N for transient flow problems. 
        http://petrowiki.org/Laplace_transformation_for_solving_transient_flow_problems
        Return list with the Stehfest coefficients'''
    import math
    ln2 = math.log(2.0)
    N2 = N / 2 
    NV = 2 * N2
    sign = 1
    V = [None]*N
    if (N2 % 2) != 0:
        sign = -1 
    for i in range(int(NV)):
        kmin = (i + 2) / 2
        kmax = i + 1
        if (kmax > N2): 
            kmax = N2
        V[i] = 0 
        sign = -sign 
        for k in range(int(kmin), int(kmax+1)):
            V[i] = V[i] + (math.pow(k, N2) / math.factorial(k)) * (math.factorial(2 * k) / math.factorial(2 * k - i - 1)) / math.factorial(N2 - k) / math.factorial(k - 1) / math.factorial(i + 1 - k)
        V[i] = sign * V[i]

        
if __name__ == "__main__":
    import sys
    print(stehfestCoeff(int(sys.argv[1])))
    


