from random import *
import cmath
import math

x=uniform(10,50)
y=uniform(10,50)

a=eval('%f+%fj'%(x,y))

r,p=cmath.polar(a)
p=math.degrees(p)
print ('{0:7.2f}'.format(a))
print('{0:7.2f}'.format(r))
print('{0:7.2f}'.format(p))

