def solution(myString, pat):    
    return int(pat.replace('A', 'b').replace('B', 'a') in myString.lower())