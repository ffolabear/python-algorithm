def solution(hp):
    general = 5
    soldier = 3
    worker = 1
    count = 0
    while hp >= general:
        hp -= general
        count += 1

    while hp >= soldier:
        hp -= soldier
        count += 1

    while hp >= worker:
        hp -= worker
        count += 1

    answer = count
    return answer


if __name__ == '__main__':
    solution(23)
