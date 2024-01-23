import sys
sys.stdin = open('노드의합구하기.txt', 'r')

V, howmany, pos = map(int, input().split())
Tree = [0 for i in range(V+1)]

for i in range(howmany):
    where, what = map(int, input().split())
    Tree[where] = what

for i in range(V-howmany, 0, -1):
    Tree[i] = Tree[i*2] + Tree[i*2+1]

print(Tree)