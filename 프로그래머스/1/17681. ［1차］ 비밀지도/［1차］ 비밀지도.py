def solution(n, arr1, arr2):
    answer = []
    check1 = []
    check2 = []

    for i in range(n):
        num = ''
        while(arr1[i] > 0):
            num = str(arr1[i] % 2) + num
            arr1[i] = arr1[i]//2
        check1.append(num.zfill(n))

    for i in range(n):
        num = ''
        while(arr2[i] > 0):
            num = str(arr2[i] % 2) + num
            arr2[i] = arr2[i]//2
        check2.append(num.zfill(n))

    for i in range(n):
        row = ''
        for j in range(n):
            if check1[i][j] == '1' or check2[i][j] == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)

    return answer
