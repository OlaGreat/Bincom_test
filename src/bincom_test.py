import random

monday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM",
          "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
print(f"mean color monday = BLUE worn {6} times")

tuesday = ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE",
           "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]
print(f"mean color tuesday = BLUE worn {6} times")

wednesday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE",
             "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]
print(f"mean color wednesday = BLUE worn {5} times")

thursday = ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM",
            "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]

print(f"mean color thursday = BLUE worn {7} times")

friday = ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED",
          "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
print(f"mean color friday = BLUE worn {6} times")

print(f"the mostly worn colour is BLUE it was worn {30} times during the week")

colors = ["ARSH", "BLACK", "BLUE", "BROWN", "CREAM", "GREEN", "ORANGE", "PINK", "RED", "WHITE", "YELLOW"]

print(f"After rearranging colours alphabetically there are {len(colors)} colours in total and the median colour"
      f" is GREEN ")

print(f"there are 95 data in total and 9 REDS, if RED is to be taken the probability will be {9 / 95} ")


def searching_algorithm(list_number: [], user_input: int):
    list_number.sort()
    list_len = len(list_number)
    low = list_number[0]
    high = list_number[-1]

    if user_input < low or user_input > high:
        print("your input is not on the list")
    else:
        if list_len % 2 != 0:
            mid_index = int(list_len / 2)
            mid_number = list_number[mid_index]
            if user_input == mid_number:
                print(f"your number was found at index {mid_index}")
            elif user_input < mid_number:
                for i in range(0, mid_index):
                    if user_input == list_number[i]:
                        print(f"your number was found at index {i}")
            elif user_input > mid_number:
                for i in range(mid_index + 1, len(list_number)):
                    if user_input == list_number[i]:
                        print(f"your number was found at index {i}")
        else:
            mid_index = int(len(list_number) / 2) - 1
            mid_number = list_number[mid_index]
            if user_input > mid_number:
                for i in range(mid_index + 1, len(list_number)):
                    if user_input == list_number[i]:
                        print(f"your number was found at index {i}")
            else:
                for i in range(0, mid_index + 1):
                    if user_input == list_number[i]:
                        print(f"your number was found at index {i}")


lia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

searching_algorithm(lia, 3)


def generate_and_covert_to_base10():
    random_number1 = random.randint(0, 1)
    random_number2 = random.randint(0, 1)
    random_number3 = random.randint(0, 1)
    random_number4 = random.randint(0, 1)

    number_base10 = random_number1 * 2 ** 3 + random_number2 * 2 ** 2 + random_number3 * 2 ** 1 + random_number4 * 2 ** 0

    print(f"{random_number1}{random_number2}{random_number3}{random_number4} to base10 is {number_base10}")


generate_and_covert_to_base10()


def fibonacci():
    previous_number = 0
    current_number = 1
    print(previous_number)
    print(current_number)
    for i in range(3, 51):
        fib = previous_number + current_number
        previous_number = current_number
        current_number = fib
        print(fib)

fibonacci()
