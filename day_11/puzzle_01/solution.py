import math
from day_11.monkey import Monkey
from day_11.monkey_pack import MonkeyPack

def process_list(monkeys: list[Monkey], round_count: int):
    monkey_pack = MonkeyPack(monkeys)
    for i in range(0, round_count):
        monkey_pack.execute_round()
    return monkey_pack.monkey_business(2)

if __name__ == "__main__":
    monkeys = [
        Monkey(
        [61],
        lambda x: x * 11,
        lambda y:  7 if y % 5 == 0 else 4,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [76, 92, 53, 93, 79, 86, 81],
        lambda x: x + 4,
        lambda y:  2 if y % 2 == 0 else 6,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [91, 99],
        lambda x: x * 19,
        lambda y: 5 if y % 13 == 0 else 0,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [58, 67, 66],
        lambda x: x * x,
        lambda y: 6 if y % 7 == 0 else 1,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [94, 54, 62, 73],
        lambda x: x + 1,
        lambda y: 3 if y % 19 == 0 else 7,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [59, 95, 51, 58, 58],
        lambda x: x + 3,
        lambda y: 0 if y % 11 == 0 else 4,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [87, 69, 92, 56, 91, 93, 88, 73],
        lambda x: x + 8,
        lambda y: 5 if y % 3 == 0 else 2,
        lambda z: int(math.floor(z/3))
        ),
        Monkey(
        [71, 57, 86, 67, 96, 95],
        lambda x: x + 7,
        lambda y:  3 if y % 17 == 0 else 1,
        lambda z: int(math.floor(z/3))
        )
    ]

    with open("./input.txt", "r", encoding="utf-8") as input_file:
        answer = process_list(monkeys, 20)
    print(f"Answer is: {answer}")
