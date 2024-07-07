import numpy as np 
rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of cols : "))
arr = np.zeros((rows,cols),dtype="int")
print("enter elements row-wise: ")

for i in range(rows):
    for j in range(cols):
        arr[i][j]=int(input())
print(arr)

def even(arr):
    evens=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if((arr[i][j])%2==0):
                evens.append(arr[i][j])
    return evens
print(even(arr))
