def solution(array):
    array.sort()
    answer = array[len(array) // 2]
    print(answer)
    return answer


if __name__ == '__main__':
    solution([1, 2, 7, 10, 11])
