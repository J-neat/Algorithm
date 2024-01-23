# sum
def getSum(n):
    if(n==1):
        return 1
    else:
        return n+getSum(n-1)


print(getSum(6))

#Fibonacci
def getFib(n):
    if(n==0):
        return 1
    elif(n==1):
        return getFib(0)
    else:
        return getFib(n-1)+getFib(n-2)

print(getFib(10))

#Factorial
def getFac(n):
    if(n==1):
        return 1
    elif(2<=n):
        return n*getFac(n-1)

print(getFac(6))

# #DFS Using Stack 수업 자료 완벽하게 짜진 코드 아님
#
# def findnext(here):
#
# print(here)
# visited[here] = True
#
# while here:
#     next = findnext(here)
#     if next:
#         push(here)
#     while next:
#         here = next
#         print(here)
#         visited[here] = True
#         next = findnext(here)
#         if next:
#             push(here)
#     here = pop()
# #here이 none 이면 끝
#책 보고 직접 짜보기
import sys
sys.stdin = open('../input.txt', 'r')

Y, X = map(int, input().split())
Data = [list(map(int, input().split())) for i in range(Y)]
##Y는 가로 X는 세로

print(Data)
start = 1
visited = [False]*Y
stack = []*Y
MyMap = [[0]*6]*7
print(MyMap)

visited[start] = 1


# def findNext(here):
#
#
#
# while(here):
#     here = findNext(start)