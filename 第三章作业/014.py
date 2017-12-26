import math

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
y3=float(input())


l1=math.sqrt((x1-x2)**2+(y1-y2)**2)
l2=math.sqrt((x2-x3)**2+(y2-y3)**2)
l3=math.sqrt((x1-x3)**2+(y1-y3)**2)

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1 and l1-l2<l3 and l1-l3<l2 and l2-l3<l1:

    L = l1+l2+l3
    p = L/2
    s = math.sqrt(p*(p-l1)*(p-l2)*(p-l3))
    print (L,s)
else:
    print ('WRONG')

