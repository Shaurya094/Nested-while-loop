num = int(input("Enter a number: "))
binary = ""
if num == 0:
    binary = "0"
else:
    while num > 0:
        re = num % 2 
        binary = str(re) + binary
        num = num // 2 
    
print ("The binary form is: ", binary)