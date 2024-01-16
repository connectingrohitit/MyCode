# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


def prefix(words: List[str]) -> str:
    str_prefix = ''
    sorted_words = sorted(words)
    first = sorted_words[0]
    last = sorted_words[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return str_prefix
        str_prefix += first[i]
    return str_prefix


print(prefix(['flex', 'flower', 'flight', 'fleow']))
