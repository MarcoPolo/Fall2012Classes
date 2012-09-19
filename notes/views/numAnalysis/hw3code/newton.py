import math

def newtons(p0, fun, dfun, n):
    for i in range(n):
        p = p0 - fun(p0)/dfun(p0)
        print p
        if abs(p - p0) < tol:
            print "Done"
            break
        p0 = p

def secant(p0,p1,fun,n):
    q0 = fun(p0)
    q1 = fun(p1)

    for i in range(n):

        p = p1 - q1*(p1 - p0)/( q1 - q0)
        print p
        if abs(p - p1) < tol:
            print "Done"
            break
        q0 = q1
        q1 = fun(p)
        p0 = p1
        p1 = p




if __name__ == "__main__":

    n = 10
    tol = 10e-5

    fun = lambda x: 2*x*math.cos(2*x) - pow((x-2),2)
    dfun = lambda x: 2*math.cos(2*x) - 4*x*math.sin(2*x) - 2*(x-2)
    p0 = 3
    p1 = 4

    #p = newtons(p0, fun, dfun, n)
    secant(p0, p1, fun, n)
