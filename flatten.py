def flatten_list(arr: list):
    flatten = list()
    for x in arr:
        if isinstance(x, list):
            # need to use extend method for extending sublist while recursion
            flatten.extend(flatten_list(x))
        else:
            flatten.append(x)
    return flatten


if __name__ == "__main__":
    arr = [1, [2, [3, 4], 5], 6]
    print(flatten_list(arr))
    exit(0)
