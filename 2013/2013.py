#定义判断是质数的函数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
#输出1000以内的质数，并计算逆序数之和
s=0
counter = 0
max = 0
min = 10000
for i in range (100,1000):
    if isPrime(i):
        print ('{0:<5}'.format(i),end='')
        #计算逆序数之和
        s1 = str(i)
        s2 = s1[::-1]
        s += int (s2)
        #控制一行输出十个数
        counter += 1
        if counter % 10 == 0:
            print()
        #得出最大值和最小值
        if int(s2) > max:
            max = int (s2)
        if int (s2) < min:
            min = int (s2)

print()


print ('平均值为{0}'.format((s-max-min)/(counter-2)))














