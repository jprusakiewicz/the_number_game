from itertools import groupby
from typing import List

from utils import list_to_chunks


def check_second_condition(digits_list: List[int]) -> bool:
    """
    Going from left to right, the digits never decrease; they only ever increase or stay the same.
    :param digits_list:
    :return: bool
    """
    single_digits_from_number = [k for k, g in groupby(digits_list)]
    chunks = list_to_chunks(single_digits_from_number)
    for chunk in chunks:
        if chunk[1] < chunk[0]:
            return False
    return True
