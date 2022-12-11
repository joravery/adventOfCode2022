import math
import day_11.puzzle_01.solution as s
from day_11.monkey import Monkey

PUZZLE_01_TEST = [
    Monkey(
        items=[79, 98],
        inspection_function=lambda x: x * 19,
        test_function=lambda y: 2 if y % 23 == 0 else 3,
        worry_reduction_function=lambda z: int(math.floor(z/3))
    ),
    Monkey(
        items=[54, 65, 75, 74],
        inspection_function=lambda x: x + 6,
        test_function=lambda y: 2 if y % 19 == 0 else 0,
        worry_reduction_function=lambda z: int(math.floor(z/3))
    ),
    Monkey(
        items=[79, 60, 97],
        inspection_function=lambda x: x * x,
        test_function=lambda y: 1 if y % 13 == 0 else 3,
        worry_reduction_function=lambda z: int(math.floor(z/3))
    ),
    Monkey(
        items=[74],
        inspection_function=lambda x: x + 3,
        test_function=lambda y: 0 if y % 17 == 0 else 1,
        worry_reduction_function=lambda z: int(math.floor(z/3))
    ),
]

TEST_PRODUCT_DIVISOR = 23 * 19 * 13 * 17
PUZZLE_02_TEST = [
    Monkey(
        [79, 98],
        inspection_function=lambda x: x * 19,
        test_function=lambda y: 2 if y % 23 == 0 else 3,
        worry_reduction_function=lambda z: z % TEST_PRODUCT_DIVISOR
    ),
    Monkey(
        [54, 65, 75, 74],
        inspection_function=lambda x: x + 6,
        test_function=lambda y: 2 if y % 19 == 0 else 0,
        worry_reduction_function=lambda z: z % TEST_PRODUCT_DIVISOR
    ),
    Monkey(
        [79, 60, 97],
        inspection_function=lambda x: x * x,
        test_function=lambda y: 1 if y % 13 == 0 else 3,
        worry_reduction_function=lambda z: z % TEST_PRODUCT_DIVISOR
    ),
    Monkey(
        [74],
        inspection_function=lambda x: x + 3,
        test_function=lambda y: 0 if y % 17 == 0 else 1,
        worry_reduction_function=lambda z: z % TEST_PRODUCT_DIVISOR
    ),
]


def test_first_provided_input():
    assert s.process_list(PUZZLE_01_TEST, 20) == 10605


def test_puzzle_02():
    assert s.process_list(PUZZLE_02_TEST, 10000) == 2713310158
