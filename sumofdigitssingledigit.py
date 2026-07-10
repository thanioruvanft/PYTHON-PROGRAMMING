num=int(input("enter the number:"))
while(num//10>0):
    sum=0
    while(num>0):
        digit=num%10
        sum=sum+digit
        num=num//10
    num=sum
print("sum of digits in single digit is :",sum)