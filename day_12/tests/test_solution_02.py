import day_12.puzzle_02.solution as s

FIRST_PROVIDED_INPUT = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

def test_puzzle_01():
    assert s.process_list(FIRST_PROVIDED_INPUT, "E", "S") == 31

def test_puzzle_02():
    assert s.process_list(FIRST_PROVIDED_INPUT, "E", "a") == 29
