def solution(want, number, discount):
    answer = 0
    want_dict = {want[i]: number[i] for i in range(len(want))}
    for i in range(len(discount) - 9):
        temp_dict = {}
        for item in discount[i:i+10]:
            if item in temp_dict:
                temp_dict[item] += 1
            else:
                temp_dict[item] = 1
        for item, quantity in want_dict.items():
            if item not in temp_dict or temp_dict[item] < quantity:
                break
        else:
            answer += 1
            
    return answer
