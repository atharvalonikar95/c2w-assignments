import numpy as np 
rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of cols : "))
arr = np.zeros((rows,cols),dtype="int")
print("enter elements row-wise: ")

for i in range(rows):
    for j in range(cols):
        arr[i][j]=int(input())
print(arr)
l=[]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i!=0 and i!=len(arr)-1 and  j!=0 and j!=len(arr)-1:
            l.append(arr[i][j])
print(l)
