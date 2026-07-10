num=int(input("enter the number:"))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
print("armstrong number :",sum)
if sum==num:
    print(sum,"is the number is armstrong number")
else:
    print(sum,"is not the armstrong number")