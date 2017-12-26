import math

x1=float(input())
y1=float(input())
r=float(input())

x2=float(input())
y2=float(input())


l=math.sqrt((x1-x2)**2+(y1-y2)**2)

if l <= r:
    print('inside')

else:
    print('outside')













