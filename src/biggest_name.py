from typing import List


def find_biggest_name(names: List[str]) -> str:
    result = names[0]
    for name in names:
        if len(name) > len(result):
            result = name

    return result
