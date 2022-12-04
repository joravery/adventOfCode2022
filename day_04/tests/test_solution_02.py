import day_04.puzzle_02.solution as s

def test_contains_overlap():
    assert s.contains_overlap("1-3", "3-7") is True
    assert s.contains_overlap("1-3", "4-7") is False
    assert s.contains_overlap("6-9", "1-2") is False
    assert s.contains_overlap("52-52", "53-53") is False
    assert s.contains_overlap("52-52", "52-53") is True
