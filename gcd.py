def computegcd(a,b):
    if b==0:
        return a
    else:
        return computegcd(b,a%b)

computegcd(125,275)
    
