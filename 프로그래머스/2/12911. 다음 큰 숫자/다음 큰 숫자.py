def solution(n):
    check_1 = format(n, 'b').count('1')
    while True:
        n += 1
        if format(n, 'b').count('1') == check_1:
            return n
