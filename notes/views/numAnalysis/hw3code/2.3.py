import math
from decimal import *

def newtons(p0, fun, dfun,tol, n):
    for i in range(n):
        p = p0 - fun(p0)/dfun(p0)
        print str(i+1)+"\t"+str(p)
        if abs(p - p0) < tol:
            print "Done"
            break
        p0 = p

def secant(p0,p1,fun,tol,n):
    q0 = fun(p0)
    q1 = fun(p1)

    for i in range(n):

        p = p1 - q1*(p1 - p0)/( q1 - q0)
        print str( i )+"\t"+str(p)
        if abs(p - p1) < tol:
            print "Done"
            break
        q0 = q1
        q1 = fun(p)
        p0 = p1
        p1 = p


def false(p0,p1,fun,tol,n):
    q0 = fun(p0)
    q1 = fun(p1)
    for i in range(n):
        p = p1 - q1*(p1 - p0)/( q1 - q0)
        print str( i+1 )+"\t"+str(p)
        if abs(p - p1) < tol:
            print "Done"
            break

        q = fun(p)
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q


if __name__ == "__main__":

    n = 10
    tol = 10e-16

    fun = lambda x: 2*x*math.cos(2*x) - pow((x-2),2)
    dfun = lambda x: 2*math.cos(2*x) - 4*x*math.sin(2*x) - 2*(x-2)
    
    fun = lambda x: pow(3,(3*x+1))-7*pow(5,(2*x))
    dfun = lambda x: math.log(3)*pow(3,(3*x+2)) - 14*math.log(5)*pow(25,(x))

    fun = lambda x: 1/x

    p0 = 0.
    #newtons(p0, fun, dfun,tol, n)
    #false(2, 3, fun,tol,n)
    #false(3, 4, fun,tol,n)

    for i in range(n):
        p = fun(float(i+1))
        print p
        if abs(p-p0) <= 5e-2:
            print "done"
        p0=p
        
