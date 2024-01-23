# # 2x3 크기의 2차원 배열 선언
# rows = 2
# cols = 3
#000
#000 이런식으로 만들어짐
# # 초기화하지 않은 2차원 배열
# matrix = [[0] * cols for _ in range(rows)]

import sys

sys.stdin = open('../input.txt', 'r')

1.한줄에 숫자 한개
[입력예]
3
[코드]

a = int(input())

[결과]
a = 3

2.한줄에 숫자 두 개 이상을 변수에 저장
[입력예]
3
5
[코드]
a, b = map(int, input().split())
[결과]
a = 3, b = 5
3.
여러개의 숫자를 정수형으로 리스트에 저장
[입력예]
1
3
5
7
9
[코드]
Data = list(map(int, input().split()))
[결과]
Data = [1, 3, 5, 7, 9]
4.
여러 개의 공백 없는 숫자를 한 자리의 숫자로 정수형으로 리스트에 저장
[입력예]
13579
[코드]
Data = list(map(int, input()))
[결과]
Data = [1, 3, 5, 7, 9]
5.
행 개수 Y과 열 개수 X가 주어지고 Y줄에 걸쳐 데이터가 주어질 때 이차리스트에 저장
[입력예]
행(Y) 은 4
열(X) 은 3
4 3
1 2 3
4 5 6
7 8 9
10 11 12
[코드]
Y, X = map(int, input().split())
Data = [list(map(int, input().split())) for i in range(Y)]
[결과]
Y = 4, X = 3
Data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]