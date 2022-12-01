import day_01.puzzle02.solution as s

def test_basic_happy_path():
    max_calories = s.top_three(["7", "\n", "2", "\n", "1", "\n"])
    assert(max_calories == [7, 2, 1])

def test_answer_is_sorted():
    max_calories = s.top_three(["2", "\n", "7", "\n", "1", "\n"])
    assert(max_calories == [7, 2, 1])

def test_max_is_single_entry():
    max_calories = s.top_three(["1", "\n", "2", "5", "\n", "33", "\n"])
    assert(max_calories == [33, 7, 1])

def test_no_max_is_zero():
    max_calories = s.top_three(["\n"])
    assert(max_calories == [0, 0, 0])

def test_duplicates():
    max_calories = s.top_three(["3", "\n", "3", "\n", "1", "1", "1", "\n"])
    assert(max_calories == [3, 3, 3])

def test_only_two_elves():
    max_calories = s.top_three(["3", "\n", "9", "\n"])
    assert(max_calories == [9, 3, 0])