
def get_book_txt(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

def get_words_count(text: str) -> int:
    words: list = text.split()
    return len(words)

def count_chars(text: str) -> list[dict[str, str | int]]:
    chars: dict[str, int] = {}
    result: list[dict[str, str | int]] = []
    i: int = 0
    for char in text:
        chars[char.lower()] = chars.get(char.lower(), 0) + 1

    for c, n in chars.items():
        result.append({"char": repr(c), "count": n})
        i += 1
    result.sort(key=lambda x: x["count"], reverse=True)
    return result

