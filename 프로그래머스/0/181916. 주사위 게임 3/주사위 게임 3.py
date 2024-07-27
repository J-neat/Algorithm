def solution(a, b, c, d):
    dice_list = [a, b, c, d]
    non_dup_list = list(set(dice_list))
    if len(non_dup_list) == 1:
        return 1111 * non_dup_list[0]
    elif len(non_dup_list) == 2:
        for element in dice_list:
            if dice_list.count(element) == 3:
                p = element
                q = [x for x in non_dup_list if x != p][0]
                return (10*p+q)**2
            elif dice_list.count(element) == 2:
                p = element
                q = [x for x in non_dup_list if x != p][0]
                return (p + q)*(abs(p-q))
    elif len(non_dup_list) == 3:
        for element in dice_list:
            if dice_list.count(element) == 2:
                new_list = [x for x in non_dup_list if x != element]
                return new_list[0]*new_list[1]
    else:  
        return min(dice_list)