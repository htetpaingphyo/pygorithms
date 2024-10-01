def merge_dicts(x: dict, y: dict) -> dict:
    x.update(y)
    return x


if __name__ == "__main__":
    x = {"a": 1, "b": 2}
    y = {"b": 3, "d": 4}
    print(merge_dicts(x, y))
