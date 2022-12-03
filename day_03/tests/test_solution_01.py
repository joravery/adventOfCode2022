import day_03.puzzle_01.solution as s

def test_find_duplicate():
    assert s.find_duplicate("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"    
    assert s.find_duplicate("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert s.find_duplicate("PmmdzqPrVvPwwTWBwg") == "P"
    assert s.find_duplicate("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"
    assert s.find_duplicate("ttgJtRGJQctTZtZT") == "t"
    assert s.find_duplicate("CrZsJsPPZsGzwwsLwLmpwMDw") == "s"

def test_get_value():
    assert s.get_value("p") == 16
    assert s.get_value("L") == 38
    assert s.get_value("P") == 42
    assert s.get_value("v") == 22
    assert s.get_value("t") == 20
    assert s.get_value("s") == 19
