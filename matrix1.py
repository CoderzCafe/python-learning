## import numpy
import numpy as np

## matrix declaration
A = [
    [1, 4, 5],
    [-5, 8, 9]
]

## numpy array
row0 = np.array(A[0])
row1 = np.array(A[1])

print("first row: " +str(row0))
print("second row: " +str(row1)+"\n")

## column (empty list)
c0 = []
c1 = []
c2 = []

for row in A:
    c0.append(row[0])
    c1.append(row[1])
    c2.append(row[2])

column0 = np.array(c0)
column1 = np.array(c1)
column2 = np.array(c2)

print("first column: " +str(column0))
print("second column: " +str(column1))
print("third column: " +str(column2))

## what an array
npA = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("\n\nThe matrix is: \n" +str(npA))

c0 = []
c1 = []
c3 = []

# numpy array rows and columns
for row in npA:
    c0.append(row[0])
    c1.append(row[1])
    c2.append(row[2])
    c3.append(row[3])

print("\n\nrow[0]: ", str(npA[0]), "\nrow[1]: ", str(npA[1]),  "\nrow[2]: ", str(npA[2]), "\nrow[3]: ", str(npA[3]))
print("\ncolumn[0]: ", str(c0), "\ncolumn[1]: ", str(c1),  "\ncolumn[2]: ", str(c2),"\ncolumn[3]: ", str(c3))

