# Basic Python Program

# print sum of 10 natural numbers using Loop

num = int(input("Enter a number: "))

if num <= 0:
    print("Enter a positive number.")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is: ", sum)      # 10 + 9 + 8 + 7 + 6+5+4+ 3 + 2 + 1 = 55

