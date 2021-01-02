from itertools import groupby
from typing import List


def group_by_identical_digits(digits_list: List[int]) -> List[List[int]]:
    return [list(g) for k, g in groupby(digits_list)]


def list_to_chunks(digits: List[int], chunk_len=2) -> List[List[int]]:
    step = 1
    chunks = []
    for i in range(0, len(digits) - chunk_len + step, step):
        chunk = digits[i: i + chunk_len]
        chunks.append(chunk)
    return chunks


def number_to_digits_list(number: int) -> List[int]:
    return [int(d) for d in str(number)]
