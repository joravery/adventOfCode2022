import math
import day_11.puzzle_01.solution as s
from day_11.monkey import Monkey

PUZZLE_01_TEST = [
    Monkey(
        [79, 98],
        lambda x: x * 19,
        lambda y: 2 if y % 23 == 0 else 3,
        lambda z: int(math.floor(z/3))
    ),
    Monkey(
        [54, 65, 75, 74],
        lambda x: x + 6,
        lambda y: 2 if y % 19 == 0 else 0,
        lambda z: int(math.floor(z/3))
    ),
    Monkey(
        [79, 60, 97],
        lambda x: x * x,
        lambda y: 1 if y % 13 == 0 else 3,
        lambda z: int(math.floor(z/3))
    ),
    Monkey(
        [74],
        lambda x: x + 3,
        lambda y: 0 if y % 17 == 0 else 1,
        lambda z: int(math.floor(z/3))
    ),
]

TEST_PRODUCT_DIVISOR = 23 * 19 * 13 * 17
PUZZLE_02_TEST = [
    Monkey(
        [79, 98],
        lambda x: x * 19,
        lambda y: 2 if y % 23 == 0 else 3,
        lambda z: z % TEST_PRODUCT_DIVISOR
    ),
    Monkey(
        [54, 65, 75, 74],
        lambda x: x + 6,
        lambda y: 2 if y % 19 == 0 else 0,
        lambda z: z % TEST_PRODUCT_DIVISOR
    ),
    Monkey(
        [79, 60, 97],
        lambda x: x * x,
        lambda y: 1 if y % 13 == 0 else 3,
        lambda z: z % TEST_PRODUCT_DIVISOR
    ),
    Monkey(
        [74],
        lambda x: x + 3,
        lambda y: 0 if y % 17 == 0 else 1,
        lambda z: z % TEST_PRODUCT_DIVISOR
    ),
]


def test_first_provided_input():
    assert s.process_list(PUZZLE_01_TEST, 20) == 10605


def test_puzzle_02():
    assert s.process_list(PUZZLE_02_TEST, 10000) == 2713310158
