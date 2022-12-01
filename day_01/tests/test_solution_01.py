import day_01.puzzle01.solution as s

def test_basic_sum():
    max_calories = s.find_max(["1", "\n", "2", "5", "\n"])
    assert max_calories == 7

def test_max_is_single_entry():
    max_calories = s.find_max(["1", "\n", "2", "5", "\n", "33", "\n"])
    assert max_calories == 33

def test_no_max_is_zero():
    max_calories = s.find_max(["\n"])
    assert max_calories == 0

def test_duplicates():
    max_calories = s.find_max(["3", "\n", "3", "\n"])
    assert max_calories == 3
