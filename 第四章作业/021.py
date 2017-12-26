n=eval(input('请输入一个整数：'))
x=1
print('\\',end='\t')

while x<=n:
    print (x,end='\t')
    x+=1
else:
    print('Done',end='\n')
y=1
for i in range(1,n):
    y=y*i
    print(y,end='\t')






