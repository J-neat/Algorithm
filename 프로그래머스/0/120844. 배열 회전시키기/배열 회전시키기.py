def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0,numbers[-1])
        numbers.pop()
        return numbers 
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
        return numbers