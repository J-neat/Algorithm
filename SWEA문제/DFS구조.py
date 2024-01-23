# 깊이 우선 탐색 중간고사에 나옴
import sys
sys.stdin = open("../input8.txt", "r")

V, E = map(int, input().split())

MyMap = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
Visited = [False] * (V + 1)

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

def DFS(here):
    print(here)
    Visited[here] = True

    for next in range(1, V + 1):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)

DFS(8)

# 재귀 호출
# def Solve(count):
#     if count == 0 : return
#     Solve(count-1)
#     print("재귀호출", count)
#
# Solve(3)

#계단 오르기 p.91
# ans = 0
# def getSome(here):
#     global ans
#     if here > howmany : return
#     if here == howmany:
#         ans += 1
#         return
#     getSome(here+1)
#     getSome(here + 2)#최대 2칸 이기 때문
#
#
# howmany = 4
# getSome(0)
# print(ans)
#DFS
