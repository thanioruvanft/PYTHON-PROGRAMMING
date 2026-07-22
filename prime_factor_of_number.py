num = int(input("Enter number: "))
i = 2
print("Prime factors are:")
while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num //= i
    else:
        i += 1
