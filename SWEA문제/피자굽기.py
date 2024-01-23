import sys
sys.stdin = open("피자굽기.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = [(i+1, cheese[i]) for i in range(N)]
    pizza_idx = N

    while len(oven) > 1:
        idx, c = oven.pop(0)
        c = c//2#치즈 오븐 들어가면 반으로 됨.
        if c == 0:
            if pizza_idx < M:
                oven.append((pizza_idx+1, cheese[pizza_idx]))
                pizza_idx += 1
        else:
            oven.append((idx, c))
    print(f"#{test_case} {oven[0][0]}")
