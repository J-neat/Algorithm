import sys
sys.stdin = open('트리연습.txt', 'r')

V, E = map(int, input().split())

Tree = [[0]*2 for _ in range(V+1)]

Data = list(map(int, input().split()))

for i in range(E):
    parent, child = Data[2*i], Data[2*i+1] #parent=[1], child[2]
    if Tree[parent][0] == 0:
        Tree[parent][0] = child
    else:
        Tree[parent][1] = child

print(Tree)