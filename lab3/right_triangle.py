# display right triangel

# input from user
n = int(input("Enter the height of right triangle: "))

# track row number
for i in range(1,n+1):
    
#tracks number of stars in ith row
    for j in range(1,i+1):
        print("*",end="")
    print()
