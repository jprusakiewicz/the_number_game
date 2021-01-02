from first_condition import check_first_condition
from second_condition import check_second_condition
from utils import number_to_digits_list

smallest_number = 37788
highest_number = 7889999


def check_conditions(number_to_check: int) -> bool:
    digit_list = number_to_digits_list(number_to_check)
    first_condition_passed = check_first_condition(digit_list)
    second_condition_passed = check_second_condition(digit_list)
    if first_condition_passed and second_condition_passed:
        return True


def main():
    current_number = smallest_number
    digit_counter = 0
    while current_number <= highest_number:
        if check_conditions(current_number):
            digit_counter += 1
        current_number += 1
    print(digit_counter)


if __name__ == "__main__":
    main()
