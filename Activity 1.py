x = input("Enter a word: ")
y = input("Enter the letter you want to find.")
i = 0
count = 0
while (i < len(x)):
    if (x[i] == y):
        count = count + 1
    i = i + 1

print ("The total number of times ",y, "has occoured: ", count)