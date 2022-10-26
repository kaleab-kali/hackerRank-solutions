def insertionSort1(arr):
    # Write your code here
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
            print(*arr)
        arr[j+1] = key
    print(*arr) 

insertionSort1([5,8,2,7,6])