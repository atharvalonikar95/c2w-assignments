# import numpy as np
# def altSum(arr):
#     sumEle = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if (i + j) % 2 == 0: # Check if the sum of indices is even
#                 sumEle += arr[i][j]

#     return sumEle
# row = int(input("Enter Row: "))
# col = int(input("Enter Col: "))
# arr = np.zeros((row, col), dtype="int")
# print("Enter elements row-wise:")
# for i in range(row):
#     for j in range(col):
#         arr[i][j] = int(input())
# sumEle = altSum(arr)
# print("Alternate Sum:", sumEle)
# print(arr)

import numpy as np 
rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of cols : "))
arr = np.zeros((rows,cols),dtype="int")
print("enter elements row-wise: ")

for i in range(rows):
    for j in range(cols):
        arr[i][j]=int(input())
print(arr)


def altsum(arr):
    sum=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i+j)%2==0:
                sum+=arr[i][j]
    return sum

print("Alternate Sum is ",altsum(arr))
