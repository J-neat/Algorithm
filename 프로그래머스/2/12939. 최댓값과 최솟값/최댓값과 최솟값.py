def solution(s):
    max_val = 0
    min_val = 0
    number = list(map(int, s.split(" ")))
    max_val = max(number)
    min_val = min(number)
    answer = str(min_val) + " " + str(max_val)
    return answer
