from random import *

number=randint(100,1000)

print (number)
x=int(number/100)
y=int(number/10)
z=number-y*10
m=y-x*10



print(z*100+m*10+x)



