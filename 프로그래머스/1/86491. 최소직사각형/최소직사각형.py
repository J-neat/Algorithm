def solution(sizes):
    max_w = max_h = 0
    for size in sizes:
        size.sort()  # 각 명함에서 짧은 변과 긴 변을 파악하기 위해 정렬
        if size[0] > max_w:
            max_w = size[0]
        if size[1] > max_h:
            max_h = size[1]
    return max_w * max_h
