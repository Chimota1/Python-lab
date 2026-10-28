from typing import Iterable
def capitalize_words(words: Iterable[str]) -> Iterable[str]:
    return map(str.capitalize, words)

print(list(capitalize_words(["python", "java", "c++"])))