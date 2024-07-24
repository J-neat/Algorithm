def solution(a, b, c):
    answer = 0
    if a != b and a != c and b!= c:
        answer = a + b + c
    if (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        answer = (a + b + c) * (a*a + b*b + c*c)
    if a == b == c:
        answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    return answer