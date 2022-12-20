import day_20.puzzle_01.solution as s


PROVIDED_TEST_INPUT = [
    "1",
    "2",
    "-3",
    "3",
    "-2",
    "0",
    "4"
]


def test_basic_happy_path():
    assert s.process_list(PROVIDED_TEST_INPUT) == 1623178306

