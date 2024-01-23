import sys
sys.stdin = open('숨바꼭질(1697).txt', 'r')
from collections import deque

n, k = map(int, input().split())##수빈이 위치, 동생 위치
#
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# 힌트
# 수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
#이동할 수 있는 경우의 수 3가지
# #짝수 인지 홀수 인지
# 처음 수빈이의 위치 N 에서 동생의 위치 K로 가는 최단 시간을 찾는 것이다.
# 최단 시간을 찾는 것이기에 DFS, BFS를 먼저 생각할 수 있다.
# 기존 위치에서 이동하는 위치는 3가지 X - 1, X + 1, 2 x X 로 총 3가지가 있다. 즉 노드가 3개로 펼쳐져 나갈 수 있다.
# 하나의 노드가 얼마나 깊이까지 가는지 모두 확인해서 최단시간을 찾으려면 모든 경로를 다 탐색해야하므로 비효율적이다.
# 즉 DFS 보다는 BFS 임을 생각한다. 동일 시간 내에서(동일 그래프 깊이) 가장 먼저 도착하는 경우가 생겼을 때가 최적 시간임을 알 수 있다.
# BFS로 문제를 풀기로 했으니, 기존 BFS 코드를 작성한다.
# 다음 노드로 펼쳐져 가는 것이 3가지가 있으니 Queue에 append할 아이템이 3가지이다.
# 최대, 최소 값이 존재하므로 X - 1, X + 1, 2 x X 값이 범위를 넘어가지 않도록 조건문을 사용해준다.
# 방문 위치를 표시하기 위한 방법을 생각해 Array 하나를 만들어 준다.
# 각 방문에 대한 표시를 노드 깊이로 설정하면, 해당 위치까지 걸린 시간을 대표하는 값이기도 하다.
#
# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if v == k:
#             return array[v]
#         for next_v in (v-1, v+1, 2*v):
#             if 0 <= next_v < MAX and not array[next_v]:
#                 array[next_v] = array[v] + 1
#                 q.append(next_v)

def bfs(v):
    queue = [v]
    while queue:
        v = queue.pop(0)
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v <= MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                queue.append(next_v)


MAX = 100001
array = [0] * MAX
print(bfs(n))