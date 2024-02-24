def solution(s):
    answer = [0, 0] # 변환 횟수와 제거된 0의 개수를 담을 리스트입니다.

    while s != '1': # s가 '1'이 될 때까지 반복합니다.
        # 1. s에서 0을 제거하고, 제거한 0의 개수를 센 후에 answer[1]에 더합니다.
        zero_count = s.count('0')
        s = s.replace('0', '')
        answer[1] += zero_count
        
        # 2. s의 길이를 2진법으로 변환합니다.
        s = format(len(s), 'b')
        
        # 변환 횟수를 1 증가시킵니다.
        answer[0] += 1

    return answer
