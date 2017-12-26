n = int (input('please enter an integer:'))

#判断是否能被3和4
if n % 3 == 0 and n % 4 == 0:
    print ('{0}能被3和4整除'.format(n))
else:
    print ('{0}不能被3和4整除'.format(n))

#判断是几位数
counter = 0
temp = n
while temp % 10 > 0:
    temp = temp // 10
    counter +=1

#输出逆序数

temp2 = n
s = 0
counter2 = 0
while counter2 < counter:
    b = temp2 % 10
    s = s * 10 + b
    temp2 = temp2 // 10
    counter2 += 1

#输出前两问结果
print ('整数{0}是一个{1}位数，其逆序数为{2}'.format(n,counter,s))

#定义判断质数的函数
import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#输出第四问结果
counter = 0
for i in range (2,n):
    if n % i == 0 and not isPrime(i):
        counter += 1
        print('整数的所有非质数因子为:\n{0:<5}'.format(i),end='')
        if counter % 5 == 0:
                print ()

#第五问
def isJishu(n):
    if n % 2 == 0:
        return True
    else:
        return False

def ou(n):
    counter5 = 0
    for i in range (2,n,2):
        if n % i == 0:
            counter5+=1
    if counter5 == 5:
        return True
    else:
        return False

def ji(n):
    counter4 = 0
    for i in range (3,n,2):
        if n % i == 0:
            counter4+=1
    if counter4 == 4:
        return True
    else:
        return False



counter4 = 0
counter5 = 0
for i in range(2, 1001):
    for j in range (2,i,2):
        if i % j == 0:
            counter5+=1
    for p in range (3,1001,2):
        if i % p == 0:
            counter4+=1
    if counter5 == 5 and counter4 == 4:
        print (i)












