# printing hollow diamond pattern using nested loops

# size of diamond as input
n = int(input("Enter the size of diamond (odd number): "))

# printing upper part of the diamond

u = int((n+3)/2)

# track rows
for i in range(1,u):

# track initial spaces
    for j in range(1,u-i):
        print(" ", end="")
    print("*", end = "")

# track middle spaces
    for k in range(1,2*i-2):
        print(" ", end = "")
    if(i==1):
        print("")
    else:
        print("*")


# print lower part of the diamond

u = int((n+1)/2)

# track rows
for i in range(1,u):

# track initial spaces
    for j in range(1,i+1):
        print(" ", end="")
    print("*",end="")

# track middle spaces
    for k in range(1,(2*(u-i)-2)):
        print(" ",end="")
    if(i== u-1):
        print("")
    else:
        print("*")