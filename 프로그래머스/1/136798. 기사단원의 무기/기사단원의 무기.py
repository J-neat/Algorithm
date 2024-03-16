def solution(number, limit, power):
    divisors = []                             # 약수 list
    for i in range(1, number+1):              # 1부터 number까지 for loop
        divisor = 0
        for j in range(1, int(i**(1/2)) + 1): # 1부터 i의 제곱근까지 for loop
            if i % j == 0:
                divisor += 1
                if j**2 != i:                 # 제곱이 되는 수는 count 1을 하여 중복 방지.
                    divisor += 1
            if divisor > limit:               # limit값을 초과하면 power값으로 return
                divisor = power
                break
        divisors.append(divisor)
    return sum(divisors)