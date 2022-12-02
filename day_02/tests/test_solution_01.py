import day_02.puzzle_01.solution as s

def test_shape_scores():
    assert s.get_shape_score("X") == 1
    assert s.get_shape_score("Y") == 2
    assert s.get_shape_score("Z") == 3
    assert s.get_shape_score("x") == 1
    assert s.get_shape_score("y") == 2
    assert s.get_shape_score("z") == 3
    assert s.get_shape_score("a") == 0

def test_outcome_scores():
    assert s.get_outcome_score("A", "Y") == 6
    assert s.get_outcome_score("A", "X") == 3
    assert s.get_outcome_score("A", "Z") == 0
    assert s.get_outcome_score("B", "Y") == 3
    assert s.get_outcome_score("B", "X") == 0
    assert s.get_outcome_score("B", "Z") == 6
    assert s.get_outcome_score("C", "Y") == 0
    assert s.get_outcome_score("C", "X") == 6
    assert s.get_outcome_score("C", "Z") == 3
   