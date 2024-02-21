from typing import List


def find_biggest_name(names: List[str]) -> str:
    result = names[0]
    for name in names:
        if name > result:
            result = name

    return result


find_biggest_name(["felipe", "teste", "aaaaaaaaaaa", "a"])
