import sys
sys.stdin = open('트리 한걸음 더.txt', 'r')

V, E = map(int, input().split())

Tree=[[0]*5for _ in range(V+1)]##13X5짜리 만들어짐

for i in range(V+1):
    Tree[i][3] = Tree[i][4] = -1

Tree[1][4] =0
Data = list(map(int, input().split()))

for i in range(E):
    parent, child = Data[i*2], Data[i*2+1]

    if Tree[parent][0] == 0:
        Tree[parent][0] = child
        Tree[parent][2] += 1
        Tree[child][3] = parent
        Tree[child][4] = Tree[parent][4] + 1
    else:
        Tree[parent][1] = child
        Tree[parent][2] += 1
        Tree[child][3] = parent
        Tree[child][4] = Tree[parent][4] + 1
    #부모의 레벨이 3이면 내 레벨은 4이다.
    Tree[child][4] = Tree[parent][4] + 1

for i in range(4):
    print()
    for j in range(1, 13):
        if (Tree[j][4] == i):
            print(f"{j}", end=" ")