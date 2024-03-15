def solution(clothes):
    from collections import defaultdict

    # 의상의 종류별로 분류하기 위한 딕셔너리
    clothes_dict = defaultdict(int)

    # 의상을 종류별로 분류하여 각 종류별 개수를 셈
    for _, type in clothes:
        clothes_dict[type] += 1

    answer = 1
    # 각 종류별 의상의 개수에 선택하지 않는 경우 1을 더해 모두 곱함
    for count in clothes_dict.values():
        answer *= (count + 1)

    # 모두 선택하지 않는 경우 1을 빼줌
    return answer - 1
