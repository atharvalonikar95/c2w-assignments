import numpy as np 

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

arr = np.zeros((rows, cols), dtype="int")
print("Enter elements row-wise:")

for i in range(rows):
    for j in range(cols):
        arr[i][j] = int(input())

print("Array:")
print(arr)

prime_numbers = []

print("Prime numbers in the array:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if is_prime(arr[i][j]):
            prime_numbers.append(arr[i][j])

print("List of prime numbers in the array:", prime_numbers)
