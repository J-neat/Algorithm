from collections import Counter

def solution(k, tangerine):
    # Counter를 이용해 각 귤의 크기별 빈도수를 구함
    count = Counter(tangerine)
    
    # 빈도수가 높은 순으로 귤의 크기를 정렬
    sorted_tangerine = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    answer = 0
    for size, freq in sorted_tangerine:
        # k개를 초과하면 종료
        if k <= 0:
            break
        # k개를 넘지 않는다면, 해당 귤의 크기를 선택
        k -= freq
        answer += 1
    
    return answer
