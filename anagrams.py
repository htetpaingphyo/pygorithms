from collections import defaultdict


def anagram_groups(arr: list):
    # defaultdict will help to create a dictionary of missing key
    anagrams = defaultdict(list)

    for x in arr:
        s = "".join(sorted(x))
        # make anagram as key of dictionary
        anagrams[s].append(x)

    return list(anagrams.values())


if __name__ == "__main__":
    arr = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
    print(anagram_groups(arr))
