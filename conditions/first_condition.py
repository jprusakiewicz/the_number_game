from typing import List

from utils import group_by_identical_digits


def check_first_condition(digits_list: List[int]) -> bool:
    """
    There are at least two groups of identical adjacent digits (like ​11​ and ​33​ in ​1123345​)
    :param digits_list:
    :return: bool
    """
    condition_counter = 0
    grouped_digits = group_by_identical_digits(digits_list)
    for group in grouped_digits:
        if len(group) > 1:
            condition_counter += 1
    if condition_counter > 1:
        return True
    return False