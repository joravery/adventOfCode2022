from day_16.node import Node
import re


def parse_node_row(row: str):
    names = r"[A-Z]{2}"
    flow_rate = r"\d+"
    all_names = re.findall(names, row)
    name = all_names[0]
    tunnels = list(all_names[1:])
    flow_rate = int(re.search(flow_rate, row)[0])
    n = Node(name, flow_rate, tunnels)
    return n
