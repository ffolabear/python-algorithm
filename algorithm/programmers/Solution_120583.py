def solution(array, n):
    cnt_dict = {}
    for i in range(len(array)):
        cnt_dict[array[i]] = cnt_dict.get(array[i], 0) + 1

    answer = cnt_dict.get(n)
    return answer


if __name__ == '__main__':
    solution([1, 1, 2, 3, 4, 5], 1)
