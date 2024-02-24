def solution(n):
    pre = 0
    cur = 1
    for _ in range(n-1):
        pre, cur = cur, (pre + cur) % 1234567
    return cur
