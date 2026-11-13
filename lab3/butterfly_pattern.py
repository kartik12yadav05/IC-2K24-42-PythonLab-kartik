# print butterfly pattern using nested loops

n = int(input("Enter the size of the butterfly: "))

# prints upper part of the butterfly
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for k in range(1,2*(n-i)+1):
        print(" ",end="")
    for t in range(1,i+1):
        print("*",end="")
    print()


# prints lower part of the butterfly
for i in range(1,n):
    for j in range(1,n-i+1):
        print("*",end="")
    for k in range(1,2*i+1):
        print(" ",end="")
    for t in range(1,n-i+1):
        print("*",end="")
    print()

    