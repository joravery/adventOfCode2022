class Node:
    def __init__(self, name: str,  flow_rate: int, tunnels: list[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels
        self.valve_open = False
        self.previous_max = float("-inf")
        self.previous_path = []
