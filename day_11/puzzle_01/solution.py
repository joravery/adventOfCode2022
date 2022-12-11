import math
from day_11.monkey import Monkey
from day_11.monkey_pack import MonkeyPack


def process_list(monkeys: list[Monkey], round_count: int):
    monkey_pack = MonkeyPack(monkeys)
    for i in range(0, round_count):
        monkey_pack.execute_round()
    return monkey_pack.monkey_business(2)


def get_monkey_list(worry_reduction_function: callable):
    return [
        Monkey(
            [61],
            lambda x: x * 11,
            lambda y:  7 if y % 5 == 0 else 4,
            worry_reduction_function
        ),
        Monkey(
            [76, 92, 53, 93, 79, 86, 81],
            lambda x: x + 4,
            lambda y:  2 if y % 2 == 0 else 6,
            worry_reduction_function
        ),
        Monkey(
            [91, 99],
            lambda x: x * 19,
            lambda y: 5 if y % 13 == 0 else 0,
            worry_reduction_function
        ),
        Monkey(
            [58, 67, 66],
            lambda x: x * x,
            lambda y: 6 if y % 7 == 0 else 1,
            worry_reduction_function
        ),
        Monkey(
            [94, 54, 62, 73],
            lambda x: x + 1,
            lambda y: 3 if y % 19 == 0 else 7,
            worry_reduction_function
        ),
        Monkey(
            [59, 95, 51, 58, 58],
            lambda x: x + 3,
            lambda y: 0 if y % 11 == 0 else 4,
            worry_reduction_function
        ),
        Monkey(
            [87, 69, 92, 56, 91, 93, 88, 73],
            lambda x: x + 8,
            lambda y: 5 if y % 3 == 0 else 2,
            worry_reduction_function
        ),
        Monkey(
            [71, 57, 86, 67, 96, 95],
            lambda x: x + 7,
            lambda y:  3 if y % 17 == 0 else 1,
            worry_reduction_function
        )
    ]

if __name__ == "__main__":
    puzzle_01_monkeys = get_monkey_list(lambda z: int(math.floor(z/3)))
    puzzle_01_answer = process_list(puzzle_01_monkeys, 20)
    print(f"Puzzle 1 answer is: {puzzle_01_answer}")

    TEST_FUNCTION_DIVISOR_PRODUCT = 5 * 2 * 13 * 7 * 19 * 11 * 3 * 17
    puzzle_02_monkeys = get_monkey_list(
        lambda z: z % TEST_FUNCTION_DIVISOR_PRODUCT)
    puzzle_02_answer = process_list(puzzle_02_monkeys, 10000)
    print(f"Puzzle 2 answer is: {puzzle_02_answer}")
