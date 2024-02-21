from typing import List


def find_average(numbers: List[int]) -> float:
    result = 0
    for number in numbers:
        result += number

    return result / len(numbers)
