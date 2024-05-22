def solution(rsp):
    scissor = "2"
    rock = "0"
    paper = "5"

    answer = ''
    formula = {scissor: rock, rock: paper, paper: scissor}
    for i in rsp:
        answer += formula.get(i, '')

    return answer


if __name__ == '__main__':
    solution("2")
