import sys
sys.stdin = open('BubbleSort.txt', 'r')

Data = list(map(int, input().split()))

print(Data)

for i in range(len(Data)-1):
    for j in range(len(Data)-i-1):
        if(Data[j]>Data[j+1]):
            Data[j],Data[j+1] = Data[j+1], Data[j]

print(Data)