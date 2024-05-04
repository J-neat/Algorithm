cnt = 0
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt

def dfs(numbers, target, current, idx):
    global cnt
    if target == current and idx == len(numbers):
        cnt += 1
    elif idx != len(numbers):
        dfs(numbers, target, current + numbers[idx], idx+1)
        dfs(numbers, target, current - numbers[idx], idx+1)