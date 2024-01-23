import sys
sys.stdin = open('MergeSort.txt', 'r')

#left : i, right : j, data: k
def mergeSort(data):
    if len(data)<=1 : return data
    left = mergeSort(data[:len(data)//2])
    right = mergeSort(data[len(data)//2:])

    i =  j =  k = 0
    while(i<len(left) and j < len(right)):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
            k += 1
        else:
            data[k] = right[j]
            j += 1
            k += 1
    return data

Data = list(map(int, input().split()))

print(mergeSort(Data))
