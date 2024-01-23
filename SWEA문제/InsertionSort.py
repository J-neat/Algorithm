import sys
sys.stdin = open('InsertionSort.txt', 'r')
#32541

Data = list(map(int, input().split()))

for here in range(1, len(Data)):
    key = Data[here] # KEY = 2

    where = here-1

    while key < Data[where] and where >= 0:
        Data[where+1] = Data[where]
        where -= 1
    Data[where+1] = key

print(Data)