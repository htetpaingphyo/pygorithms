import string


def is_palindrome(text: str) -> bool:
    text = (
        text.replace(" ", "")
        .lower()
        .translate(str.maketrans("", "", string.punctuation))
    )
    return text[::] == text[::-1]


if __name__ == "__main__":
    text = "A man, a plan, a canal, Panama"
    print(is_palindrome(text))
