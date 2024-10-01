def greatest_pair(arr: list):
    prev = count = 0
    temp = dict()
    arr.sort()

    for i in arr:
        if i == prev:
            count += 1
        else:
            count = 0
            prev = i

        if count > 0:
            temp.update({i: count})

    for key, value in temp.items():
        if value > prev:
            prev = value


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    greatest_pair(arr)
