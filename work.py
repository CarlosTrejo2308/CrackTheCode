def square(x):
    return x * x

def triple(x):
    return 3 * x

def minNum(arr):
    min = arr[0]
    for ele in arr:
        if ele < min:
            min = ele
    return min

def sumArray(arr):
    total = 0
    for ele in arr:
        total += ele
    return total

def bubbleSort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr