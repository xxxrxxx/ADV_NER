a=3
b=[1,2,3,4,5,6,7,8,9]
b1=b[::-1]
number=0
for i,num in enumerate(b1):
    number +=num*(10**i)
res=(a**number)%1300
print(res)