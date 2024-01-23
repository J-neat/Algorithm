import sys
sys.stdin = open('중위순회.txt', 'r')

def in_order(node):
    global word
    if node != 0:
        in_order(tree[node][1])
        word += tree[node][0]
        in_order(tree[node][2])

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    tree = [['', 0, 0] for _ in range(N+1)]
    word = ""
    for _ in range(N):
        data = list(map(str, input().split()))
        if len(data) == 4:
            node, char, left_node, right_node = data
            tree[int(node)] = [char, int(left_node), int(right_node)]
        elif len(data) == 2:
            node, char = data
            tree[int(node)] = [char, 0, 0]
    in_order(1)
    print("#{} {}".format(test_case, word))
