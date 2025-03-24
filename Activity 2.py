num = int(input("Enter a number: "))
flag = False

if num > 1:
    for i in range (2, num):
        if num % 1 == 0:
            flag = True
            break

if flag: 
    print (num, "isn't a prime number.")
else:
    print (num, "is a prime number.")