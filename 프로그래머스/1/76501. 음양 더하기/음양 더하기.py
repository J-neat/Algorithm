def solution(absolutes, signs):
    answer = 0
    nums = [0] * len(signs)
    for i in range(len(signs)):
        if signs[i] == True:
            nums[i] = absolutes[i]
        else:
            nums[i] = -absolutes[i]
    answer = sum(nums)
    return answer