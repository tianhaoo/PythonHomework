
I=int(input('输入存款，单位万元：'))
if I < 10:
    x = I*1.5/100

elif I>=10 and I<50:
    x = I*2/100

elif I>=50 and I<100:
    x = I * 3 / 100

elif I>=100:
    x = I * 3.5 / 100

sum = I + x
print (sum)



















