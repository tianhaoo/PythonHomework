x=int(input())
y=int(input())
z=int(input())

if x>=y:
    if z>x:
        print(y,x,z)
    else:
        if y>z:
            print(z,y,x)
        else:
            print(y,z,x)
else:
    if x<=z:
        if y<=z:
            print (x,y,z)
        else:
            print (x,z,y)
    else:
        print (z,x,y)
