import sys
sys.stdin = open('../inputZ.txt', 'r')
a, b = map(int, input().split())

abilities = list(map(int, input().split()))
abilities.sort(reverse=True)##내림차순 정렬 사용

time = 0

while a < b:
    for ability in abilities:
        if (a + ability) <= b:
            a += ability
            time += 1
            break
    else:
        time = -1
        break

print(time)
