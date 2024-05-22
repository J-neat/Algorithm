# n, m, k 공백으로 구분 입력받음
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받음
data = list(map(int, input().split()))

# 입력받은 수 정렬
data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

res = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        res += first
        m -= 1 # 더할 때마다 1씩 빼기

    if m == 0: # m이 0이라면 반복문 탈출
        break
    res += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(res)