
x = int(input ('不多于五位的正整数:'))



if x // 10==0:
    print('一位数')
    print(x)
    print(x)

elif x//100==0:
    print('二位数')
    m=x//10
    n=x%10
    print(m,n)
    print(n*10+m)


elif x//1000==0:
    print('三位数')
    m=x//100
    n=x//10%10
    p=x%10

    print(m,n,p)
    print(p*100+n*10+m)


elif x//10000==0:
    print('四位数')
    m=x//1000
    n=x//100%10
    p=x//10%10
    q=x%10
    print(m,n,p,q)


elif x//100000==0:
    print('五位数')
    m = x // 10000
    n = x // 1000 % 10
    p = x // 100 % 10
    q = x // 10 % 10
    s = x % 10
    print(m,n,p,q,s)
    print(s*10000+q*1000+p*100+n*10+m)






