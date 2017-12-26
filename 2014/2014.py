#定义判断一个数是否为完数的函数
def isWs(n):
    s = 0
    for i in range (1,n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    return False

#输出1000以内的所有完数，并找出最大的一个
m = 0
for i in range(1,1001):
    if isWs(i):
        if m < i:
            m = i
        print ('{0:<5}'.format(i),end='')
print ()

#最大完数是 m
#输出最大完数的所有因子
#计算出去掉一之后的和
counter = 0
s = 0                                  #用s来存储和
for i in range (1,m):
    if m % i == 0:
        counter += 1
        if '1' not in str(i):          #判断一是否在里面
            s += i
        print ('{0:>5}'.format(i),end = '')
        if counter % 8 == 0:           #计数器
            print ()
print ()

#计算平均值并输出最终结果
print((s-1)/(counter-1))



