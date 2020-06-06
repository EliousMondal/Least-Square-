k = int(input('Enter the degree of approximate polynomial : '))
x = float(input('Enter the value of x coordinate : '))

from mullikendata import xi
from mullikendata import yi


def g(k):
    a = 0
    b = 0
    for i in xi:
        a = a + i*u(k,i)*u(k,i)
    for i in xi:
        b = b + u(k,i)*u(k,i)
    return (a/b)

def h(k):
    a = 0
    b = 0
    if k == 0:
        return 0
    else:
        for i in xi:
            a = a + i*u(k,i)*u(k-1,i)
        for i in xi:
            b = b + u(k-1,i)*u(k-1,i)
        return (a/b)

def u(k,x):
    if k == 0:
        return 1
    elif k == 1:
        return (x-g(k-1))*u(k-1,x)
    else:
        a = ((x-g(k-1))*u(k-1,x)) - (h(k-1)*u(k-2,x))
        return a

def coeff(j):
    a = 0
    b = 0
    for i in range(len(xi)):
        a = a + u(j,xi[i])*yi[i]
    for i in range(len(xi)):
        b = b + u(j,xi[i])*u(j,xi[i])
    return (a/b)
            
def p(k,x):
    a = 0
    i = 0
    while i < k+1:
        a = a + coeff(i)*u(i,x)
        i = i + 1
    return a

print('The value of y corresponding to given x on the approximation polynomial is : ',p(k,x))
