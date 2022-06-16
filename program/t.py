def digitsSum(Number):
    Sum = rem = 0
    while Number > 0:
        rem = Number % 10
        Sum = Sum + rem
        Number = Number // 10
    return Sum

minHrd = int(input("Enter the Minimum Harshad Number = "))
maxHrd = int(input("Enter the Maximum Harshad Number = "))

print("\nThe List of Harshad Numbers from {0} and {1}".format(minHrd, maxHrd)) 
for i in range(minHrd, maxHrd + 1):
    Sum = digitsSum(i)
    if i % Sum == 0:
        print(i, end = '   ')