import numpy as np 
rows=int(input("Enter number of rows : "))
cols=int(input("Enter number of cols : "))
arr = np.zeros((rows,cols),dtype="int")
print("enter elements row-wise: ")

for i in range(rows):
    for j in range(cols):
        arr[i][j]=int(input())
print(arr)
max_values=[]
for i in range(len(arr)):
    max_values.append(max(arr[i]))
print("The values from each row are ",max_values)
    
   
