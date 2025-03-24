num = input("Enter the number: ")
if len(num) >= 4:
    mid = len(num) // 2
    mid1 = int (num[mid-1])
    mid2 = int(num(mid))
    print (f"\nProduct of Mid digits ({mid1} * {mid2}) = {mid1 * mid2}")
else:
    print ("\nIt's not a 4 or more digit number!")