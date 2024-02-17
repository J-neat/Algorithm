def solution(name, yearning, photo):
    answer = []
    my_dict = dict(zip(name, yearning))
    for people in photo:
        sum = 0
        for person in people:
            sum += my_dict.get(person, 0)
        answer.append(sum)
    return answer