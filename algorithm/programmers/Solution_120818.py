import math


def solution(price):
    answer = 0
    if 500_000 <= price:
        answer = price * 0.8
    elif 300_000 <= price < 500_000:
        answer = price * 0.9
    elif 100_000 <= price < 300_000:
        answer = price * 0.95
    else:
        answer = price
    return math.floor(answer)