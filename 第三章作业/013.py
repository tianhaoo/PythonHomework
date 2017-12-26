

a=float(input ())
b=float(input ())
c=float(input ())
m=b**2-4*a*c
if abs(a-0)<=1.0e-5:
    print ("wrong!a不能等于0")
elif m<0:
    import cmath

    print('无实数解')
    x1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print ('{0:10.5f},{1:10.5f}'.format(x1,x2))
elif m>=0:
    import math
    print('有实数解')
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print('{0:10.5f},{1:10.5f}'.format(x1, x2))
