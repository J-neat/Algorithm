import sys
sys.stdin = open('QuickSort.txt', 'r')

Data = list(map(int, input().split()))

print(Data)
def quick_sort(Data):
    if len(Data) <= 1:
        return Data
    pivot = Data[len(Data) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in Data:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


print(quick_sort(Data))