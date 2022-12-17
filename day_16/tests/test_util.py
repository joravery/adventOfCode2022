import pytest
import day_16.puzzle_01.solution as s

test_data = [
    ("Valve JJ has flow rate=21; tunnel leads to valve II", {"name": "JJ", "flow_rate": 21, "tunnels": ["II"]}),
    (
        "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
        {"name": "BB", "flow_rate": 13, "tunnels": ["CC", "AA"]},
    ),
    (
        "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
        {"name": "DD", "flow_rate": 20, "tunnels": ["CC", "AA", "EE"]},
    ),
]


@pytest.mark.parametrize("input_string,expected_dict", test_data)
def test_parse_node_row(input_string, expected_dict):
    node = s.parse_node_row(input_string)
    for attr in expected_dict.keys():
        assert getattr(node, attr) == expected_dict[attr]


#     assert node.name == "BB"
#     assert node.flow_rate == 13
#     assert node.tunnels == ["CC", "AA"]

# "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
