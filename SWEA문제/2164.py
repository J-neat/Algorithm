import sys
sys.stdin = open('2164.txt', 'r')

cardNum = int(input())

cardList = []

for i in range(1, cardNum+1):
    cardList.append(i)

print(cardList)
count = len(cardList)#처음 카드의 수

for j in range(0, count-1):
    if (len(cardList) != 1):
        cardList.pop(0)
        num = cardList[0]
        cardList.pop(0)
        cardList.append(num)

print(cardList)