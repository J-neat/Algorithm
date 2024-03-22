from collections import Counter
def solution(participants, completion):
    answer = ''
    participants_count = Counter(participants)
    completion_count = Counter(completion)
    difference = participants_count - completion_count
    answer = list(difference.keys())[0]
    return answer