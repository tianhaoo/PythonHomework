x = 1

lst = ['x'] + [str(i) for i in range(1,13)]
for i in lst:
    print('{:<10}'.format(i,end=' '))
print()

while x <= 12:
    print('{:<10}'.format(str(x)),end=' ')
    y = 1
    while y <= 12:
        print('{:<10}'.format(str(x*y),end=' ')
    y += 1
    print()
    x +=1















