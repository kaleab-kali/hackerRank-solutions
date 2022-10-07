#bubble sort answer to hackerrank solution


def countSwaps(a):
    swapped = 0
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swapped += 1
                
    print(f"Array is sorted in {swapped} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
