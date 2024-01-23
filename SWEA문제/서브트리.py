import sys
sys.stdin = open('서브트리.txt', 'r')

T = int(input())

def findNodesNum(N, edges):
    count = 1
    for i in range(0, len(edges), 2):
        if edges[i] == N:
            count += findNodesNum(edges[i+1], edges)
    return count

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    print("#{} {}".format(test_case, findNodesNum(N, edges)))
