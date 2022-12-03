import day_03.puzzle_02.solution as s

def test_get_group_badge():
    assert s.get_group_badge(["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"]) == "r"
    assert s.get_group_badge(["ttgJtRGJQctTZtZT","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","CrZsJsPPZsGzwwsLwLmpwMDw"]) == "Z"

def test_get_value():
    assert s.get_value("p") == 16
    assert s.get_value("L") == 38
    assert s.get_value("P") == 42
    assert s.get_value("v") == 22
    assert s.get_value("t") == 20
    assert s.get_value("s") == 19
