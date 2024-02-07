def solution(numbers, k):#numbers: 번호가 들어있음, k 번째로 공을 던지는 사람
    answer = 0
    if len(numbers) < k * 2:
        numbers = numbers * ((k*2) // len(numbers) + 1)

    answer = numbers[2*(k-1)]
    return answer