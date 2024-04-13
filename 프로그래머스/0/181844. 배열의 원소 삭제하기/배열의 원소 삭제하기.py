def solution(arr, delete_list):
    answer = []
    for num in delete_list:
        if num in arr:
            arr.pop(arr.index(num))
    return arr