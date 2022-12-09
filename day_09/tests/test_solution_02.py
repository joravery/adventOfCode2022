import day_09.puzzle_02.solution as s

PUZZLE_TWO_TEST = ["R 5",
"U 8",
"L 8",
"D 3",
"R 17",
"D 10",
"L 25",
"U 20"]

PUZZLE_ONE_TEST = [
"R 4",
"U 4",
"L 3",
"D 1",
"R 4",
"D 1",
"L 5",
"R 2",
]

def test_basic_happy_path():
    assert s.process_list(PUZZLE_TWO_TEST)[1] == 36
    assert s.process_list(PUZZLE_ONE_TEST)[1] == 1
