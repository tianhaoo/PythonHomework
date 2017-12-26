from math import *


(x1,y1)=eval(input())
(x2,y2)=eval(input())
(x3,y3)=eval(input())
l1=sqrt((x1-x2)**2+(y1-y2)**2)
l2=sqrt((x2-x3)**2+(y2-y3)**2)
l3=sqrt((x1-x3)**2+(y1-y3)**2)
L=(l1+l2+l3)/2
s=sqrt(L*(L-l1)*(L-l2)*(L-l3))
print (s)