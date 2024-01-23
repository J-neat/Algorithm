#Josephus Problem
#pop(0)을 써야함: 자료구조의 큐를 공부하는 것이기 때문에
# #FIFO규칙에 따라 pop(0)을 쓰는 것이 맞음
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
# 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
import sys
sys.stdin = open('JosephusProblem.txt', 'r')
N, K = map(int, input().split())

Queue =[]

for people in range(1, N):
    Queue.append(people)



while len(Queue) != K:
    alive1 = Queue.pop(0)
    alive2 = Queue.pop(0)
    dead = Queue.pop(0)
    Queue.append(alive1)
    Queue.append(alive2)

print("last = ", Queue)