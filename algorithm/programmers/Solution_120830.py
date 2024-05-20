def solution(n, k):
    k = k - n // 10
    lamb = 12_000
    drink = 2_000

    answer = lamb * n + drink * k
    return answer
