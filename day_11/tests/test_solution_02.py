import day_11.puzzle_02.solution as s
from day_11.monkey import Monkey

TEST_PRODUCT_DIVISOR = 23 * 19 * 13 * 17
FIRST_PROVIDED_INPUT = [
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
    assert s.process_list(FIRST_PROVIDED_INPUT, 10000) == 2713310158
