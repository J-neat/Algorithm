# import sys
# sys.stdin = open('숨바꼭질4.txt', 'r')
#
# Visited = [0]*100001
# queue = []
#
# def bfs():
#     N, K = map(int, input().split())
#     queue = [(N, 0)]
#     while queue:
#         N, count = queue.pop(0)
#         if N == K:
#             Visited[K] = count
#         for newN in [N+1, N-1, 2*N]:
#             if 0 <= newN <= 100000 and not Visited[newN]:
#                 Visited[newN] = 1
#                 queue.append((newN, count+1))
#     return Visited[K]
#
# print(bfs())


import sys
sys.stdin = open('숨바꼭질4.txt', 'r')

N, K = map(int, input().split())
Visited = [0]*100001
from_ = [-1]*100001  # 이전 위치를 저장
queue = []

def bfs():
    queue.append((N, 0))
    while queue:
        current, count = queue.pop(0)
        if current == K:
            path = [K]
            while current != N:  # 시작 위치에 도달할 때까지 반복
                path.append(from_[current])  # 경로에 이전 위치 추가
                current = from_[current]  # 이전 위치로 이동
            print(count)  # 걸린 시간 출력
            print(' '.join(map(str, path[::-1])))  # 경로 출력 (역순으로)
            return
        for next in [current-1, current+1, current*2]:
            if 0 <= next <= 100000 and not Visited[next]:
                queue.append((next, count+1))
                Visited[next] = 1
                from_[next] = current  # 다음 위치의 이전 위치를 현재 위치로 저장

bfs()
