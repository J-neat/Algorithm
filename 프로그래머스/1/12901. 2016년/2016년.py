def solution(a, b):
    answer = ''
    adict = {1: 31, 2: 29, 3: 31,
             4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30,
             10: 31, 11: 30, 12: 31}
    daydict = {0: "THU", 1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED"}
    days = 0
    for i in range(1, a):
        days += adict[i]
    
    days += b
    name = days % 7
    answer = daydict[name]
    return answer
