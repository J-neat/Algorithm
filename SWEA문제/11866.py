import sys
sys.stdin = open("11866.txt", 'r')
N, K = map(int, input().split())#N = 7, K = 3 (N명에서 K번째 사람 계속 죽이기)
MyList = []
dead = []
index = 0
#<1, 2, 3, 4, 5, 6, 7>
#3, 6, 2, 7, 5, 1, 4
for i in range(1,N+1):
    MyList.append(i)

while MyList:
    index = (index + (K-1)) % len(MyList)
    dead.append(str(MyList.pop(index)))

print(dead)