def find_duplicates(arr: list):
    seen = set()
    duplicates = set()

    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)

    return duplicates


if __name__ == "__main__":
    arr = [7, 4, 1, 1, 5, 8, 7, 0, 4, 2, 1]
    print(find_duplicates(arr))
