def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack and stack[-1] == "(":
            stack.pop()
        else:
            return False  # ')' 문자가 나왔는데 스택이 비어 있거나, 괄호의 짝이 맞지 않는 경우

    return len(stack) == 0  # 모든 괄호를 검사한 후 스택이 비어 있으면 올바른 괄호
