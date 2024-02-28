def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people) - 1

    while start <= end:
        # 가장 무거운 사람과 가장 가벼운 사람을 함께 태울 수 있으면
        if people[start] + people[end] <= limit:
            start += 1
        # 가장 무거운 사람만 태우고
        end -= 1
        # 보트의 수를 하나 늘린다.
        answer += 1

    return answer
