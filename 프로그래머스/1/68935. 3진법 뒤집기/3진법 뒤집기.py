def convert(n):
    num = ''
    while n > 0:
        num += str(n % 3)
        n = n // 3
    return num

def solution(n):
    num = convert(n)
    answer = int(num, 3)
    return answer
