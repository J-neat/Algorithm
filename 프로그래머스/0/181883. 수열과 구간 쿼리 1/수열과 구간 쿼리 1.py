def solution(arr, queries):
    for i, query in enumerate(queries) :
        for k in range(query[0], query[1]+1) :
            arr[k] += 1
    return arr