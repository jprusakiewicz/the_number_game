from typing import List

from conditions import check_first_condition, check_second_condition

# third condition
SMALLEST_POSSIBLE_PASSWORD = 37788
HIGHEST_POSSIBLE_PASSWORD = 7889999


def split_integer_to_digits(number: int) -> List[int]:
    return [int(d) for d in str(number)]


def check_conditions(number_to_check: int) -> bool:
    digits = split_integer_to_digits(number_to_check)
    first_condition_passed = check_first_condition(digits)
    second_condition_passed = check_second_condition(digits)
    if first_condition_passed and second_condition_passed:
        return True


def main():
    current_password = SMALLEST_POSSIBLE_PASSWORD
    possible_passwords_counter = 0
    print("counting in progress...\n")
    while current_password <= HIGHEST_POSSIBLE_PASSWORD:
        if check_conditions(current_password):
            possible_passwords_counter += 1
        current_password += 1
    print("You have to check {0} numbers".format(possible_passwords_counter))


if __name__ == "__main__":
    main()
