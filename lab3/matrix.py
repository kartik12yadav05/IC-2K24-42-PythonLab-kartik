 # MATRIX operations

number = [[0,0,0], [0,0,0], [0,0,0]]

# matrix input from user
print("------------------------------------")
print("Enter the elements of matrix: ")
for i in range(0,3):
    for j in range(0,3):
        number[i][j] = int(input())

# display matrix in proper rows and columns
sum = 0
diagnol_sum = 0
max_elem = number[0][0]
min_elem = number[0][0]
print("------------------------------------")
print("MATRIX: ")
for i in range(0,3):
    for j in range(0,3):
        print(number[i][j],"  ",end="")
        # finding sum of all elements
        sum = sum + number[i][j]
        # finding sum of main diagnol elements
        if ( i==j ):
            diagnol_sum = diagnol_sum + number[i][j]
        # finding largest element
        if (max_elem < number[i][j]):
            max_elem = number[i][j]
        # finding smallest element
        if( min_elem > number[i][j]):
            min_elem = number[i][j]
    print()
print("------------------------------------")

print("Sum of ALL elements of matrix: ", sum)
print("Sum of main DIAGNOL elements of the matrix: ", diagnol_sum)
print("LARGEST element of the matrix: ", max_elem)
print("SMALLEST element of the matrix: ", min_elem)

# transpose of matrix
print("------------------------------------")
print("TRANSPOSE MATRIX: ")
for i in range(0,3):
    for j in range(0,3):
        print(number[j][i]," ",end="")
    print()
print("------------------------------------")



