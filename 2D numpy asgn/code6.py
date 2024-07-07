import numpy as np 
rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of cols : "))
arr1 = np.zeros((rows,cols),dtype="int")
arr2 = np.zeros((rows,cols),dtype="int")

print("enter elements row-wise: ")


for i in range(rows):
    for j in range(cols):
        arr1[i][j]=int(input())
print(arr1)
print("enter elements row-wise: ")
for i in range(rows):
    for j in range(cols):
        arr2[i][j]=int(input())
print(arr2)

l=[]
for i in range (len(arr1)):
    for j in range(len(arr1[i])):
        if arr1[i][j] in arr2:
            l.append(arr1[i][j])
print("The common elements from both 2D arrays are ",l)
