import pytest
import day_16.puzzle_01.solution as s

PROVIDED_TEST_INPUT = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II",
]

SHORTENED_INPUT = [
    "Valve AA has flow rate=0; tunnels lead to valves BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves BB",
]

SHORTENED_INPUT_SKIP_REQUIRED = [
    "Valve AA has flow rate=0; tunnels lead to valves BB",
    "Valve BB has flow rate=2; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=13; tunnels lead to valves BB",
]

VALUE_EVERY_STEP = [
    "Valve AA has flow rate=0; tunnels lead to valves BB",
    "Valve BB has flow rate=2; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=1; tunnels lead to valves BB",
]

def test_value_every_step():
    assert s.process_list(VALUE_EVERY_STEP, "AA", 6) == 10

def test_value_every_step_not_enough_time():
    assert s.process_list(VALUE_EVERY_STEP, "AA", 4) == 4

def test_value_every_step_not_enough_time():
    assert s.process_list(VALUE_EVERY_STEP, "AA", 5) == 7

def test_basic_happy_path():
    assert s.process_list(PROVIDED_TEST_INPUT, "AA") == 1651

def test_short_path():
    assert s.process_list(SHORTENED_INPUT, "AA") == 416

def test_short_path_with_skipping_optimal():
    assert s.process_list(SHORTENED_INPUT_SKIP_REQUIRED, "AA") == 401

if __name__ == "__main__":
    # test_basic_happy_path()
    # test_short_path()
    test_short_path_with_skipping_optimal()
    pass
