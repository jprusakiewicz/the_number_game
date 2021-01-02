from .conditions import check_first_condition, check_second_condition
from utils import number_to_digits_list

# third condition
SMALLEST_POSSIBLE_PASSWORD = 37788
HIGHEST_POSSIBLE_PASSWORD = 7889999


def check_conditions(number_to_check: int) -> bool:
    digit_list = number_to_digits_list(number_to_check)
    first_condition_passed = check_first_condition(digit_list)
    second_condition_passed = check_second_condition(digit_list)
    if first_condition_passed and second_condition_passed:
        return True


def main():
    current_number = SMALLEST_POSSIBLE_PASSWORD
    possible_passwords_counter = 0
    print("counting in progress...\n")
    while current_number <= HIGHEST_POSSIBLE_PASSWORD:
        if check_conditions(current_number):
            possible_passwords_counter += 1
        current_number += 1
    print("You have to check {0} numbers".format(possible_passwords_counter))


if __name__ == "__main__":
    main()
