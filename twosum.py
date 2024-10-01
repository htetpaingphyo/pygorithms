# write an algorithm to return indices of an array where addition of two number match the result


def two_number(arr: list, num: int):
    indices = None
    for i in range(0, len(arr), 1):
        for j in range(0, i, 1):
            if arr[i] + arr[j] == num:
                indices = [j, i]
    return indices


if __name__ == "__main__":
    arr = [4, 8, 3, 11, 7, 6, 19]
    num = int(input("enter number: "))
    print(two_number(arr, num))
