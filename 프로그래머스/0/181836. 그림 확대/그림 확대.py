def solution(picture, k):
    answer = []
    
    for row in picture: # 이미지의 한 줄을 가져온다.
        resized = ''
        
        for pixel in row:
            resized += pixel * k # 한 픽셀을 k배 만큼 가로로 늘린다.
        
        for _ in range(k):
            answer.append(resized) # 가로로 늘려진 이미지 한 줄을 k배 만큼 세로로 늘린다. 
    
    return answer