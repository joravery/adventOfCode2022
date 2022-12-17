from day_16.util import parse_node_row

from day_16.node import Node


def process_list(lines: list, starting_node_name: str, minutes: int = 30):
    nodes = dict()
    for line in lines:
        n = parse_node_row(line)
        nodes[n.name] = n
    return find_best_path(nodes, starting_node_name, minutes)


class Attempt:
    def __init__(
        self, current_node: Node, visited_nodes: list[str], open_nodes: list[str], moves_left: int, score: int
    ) -> None:
        self.current_node = current_node
        self.visited_nodes = visited_nodes
        self.open_nodes = open_nodes
        self.moves_left = moves_left
        self.score = score


def get_max_possible_score_left(attempt: Attempt, nodes: dict[str, Node]):
    unopened_nodes = sorted(
        [node.flow_rate for node in nodes.values() if node.name not in attempt.open_nodes], reverse=True
    )
    total = 0
    ticks_left = attempt.moves_left + 1 # plus 1 to account for maybe being at a valuable node already ...
    i = 0
    while i < len(unopened_nodes) and ticks_left > 1:
        total += unopened_nodes[i] * ticks_left
        i += 1
        ticks_left -= 2

    return total


def find_best_path(nodes: dict[str, Node], starting_node: str, minutes: int):
    max_pressure = float("-inf")
    max_sequence = None
    queue: list[Attempt] = []
    current_node = nodes[starting_node]
    queue.append(Attempt(current_node, ["AA"], ["AA"], minutes, 0))
    total_scenarios_created = 1  # lol, hack to get around div0 error
    total_scenarios_completed = 0
    total_secnarios_abandoned = 0

    while len(queue) > 0:
        attempt = queue.pop()
        max_pressure = max(max_pressure, attempt.score)
        if attempt.moves_left <= 0:
            if attempt.score >= max_pressure:
                max_pressure = attempt.score
                max_sequence = attempt.visited_nodes
            total_scenarios_completed += 1
        else:
            # if get_max_possible_score_left(attempt, nodes) < (max_pressure - attempt.score):
            #     # Abandon attempts that cannot beat the current max, even if they magically opened every remaining valve on their next turn or if they cannot possibly open all remaining valuable nodes
            #     total_secnarios_abandoned += 1
            #     continue
            attempts = visit_node(nodes, attempt)
            queue += attempts
            total_scenarios_created += len(attempts) - 1  # Take one out for the parent of the visits
        print(
            f"Queue size: {len(queue):,}, max score: {max_pressure:,}, created: {total_scenarios_created:,}, completed: {total_scenarios_completed:,}, abandonded: {total_secnarios_abandoned:,}, queue % of total: {len(queue)/total_scenarios_created*100:.2f}",
            end="\r",
        )
        if total_scenarios_created % 1000000 == 0:
            print(
                f"Queue size: {len(queue):,}, max score: {max_pressure:,}, created: {total_scenarios_created:,}, completed: {total_scenarios_completed:,}, abandonded: {total_secnarios_abandoned:,}, queue % of total: {len(queue)/total_scenarios_created*100:.2f}",
                end="\r",
            )
    print(
        f"Queue size: {len(queue):,}, max score: {max_pressure:,}, created: {total_scenarios_created:,}, completed: {total_scenarios_completed:,}, abandonded: {total_secnarios_abandoned:,}, queue % of total: {len(queue)/total_scenarios_created*100:.2f}"
    )
    print(f"After completion, max score: {max_pressure}, max sequence: {max_sequence}")
    return max_pressure


def get_valuable_node_names(nodes: dict[str, Node]):
    return [node.name for node in nodes.values() if node.flow_rate > 0]


def all_valuable_nodes_open(attempt: Attempt, nodes: dict[str, Node]) -> bool:
    valuable_nodes = get_valuable_node_names(nodes)
    valuable_nodes_open = [x in attempt.open_nodes for x in valuable_nodes]
    return all(valuable_nodes_open)


def many_repeat_visits(attempt: Attempt, destinations: list[str]) -> bool:
    # if len(attempt.visited_nodes) > 5:
    #     #     # After we've visited a handful of nodes, if the top two nodes are more than 2/3rds the visits we're probably in an unproductive loop
    #     if (
    #         sum(sorted([attempt.visited_nodes.count(x) for x in set(attempt.visited_nodes)], reverse=True)[:2])
    #         > 2 * len(attempt.visited_nodes) / 3
    #     ):
    #         # print(f"**************************** skipped due to unproductive loop*******************")
    #         return True
    # If any of the destination nodes have been visited more times than we have guesses left, exit
    # for destination in destinations:
    #     if attempt.visited_nodes.count(destination) * 2 > attempt.moves_left:
    #         return True
    return False


def visit_node(nodes: dict[str, Node], attempt: Attempt):
    attempt_iterations: list[Attempt] = []
    current_node = attempt.current_node
    travel_options = current_node.tunnels

    # if all_valuable_nodes_open(attempt, nodes) or many_repeat_visits(attempt, travel_options):
    if False or many_repeat_visits(attempt, travel_options):
        # print(f"All nodes visited and open, setting remaining moves to 0")
        attempt.moves_left = 0
        attempt_iterations.append(attempt)
        return attempt_iterations

    # visit each child without opening the node, marking stuck nodes (0 value) as open
    # This option can be advantageous of there is a high-value node in the unvisited path options
    if current_node.flow_rate == 0 and current_node.name not in attempt.open_nodes:
        attempt.open_nodes.append(current_node.name)
    attempt.moves_left -= 1
    if attempt.moves_left == 0:
        return [attempt]
    if len(set(attempt.visited_nodes)) < len(nodes):
        # Only visit a node and NOT open it if we haven't visited all nodes, otherwise every visit should result in an open, and we'll finish sooner
        for destination in get_destination_nodes(attempt, travel_options, nodes):
            attempt_iterations.append(
                Attempt(
                    nodes[destination],
                    attempt.visited_nodes + [destination],
                    attempt.open_nodes,
                    moves_left=attempt.moves_left,
                    score=attempt.score,
                )
            )

    if current_node.name not in attempt.open_nodes and current_node.flow_rate > 0 and attempt.moves_left > 0:
        # open node, update score to include this node's flow rate for remaining moves
        attempt.score += attempt.moves_left * current_node.flow_rate
        attempt.moves_left -= 1
        if attempt.moves_left == 0:
            return attempt_iterations + [attempt]

        for destination in get_destination_nodes(attempt, travel_options, nodes):
            attempt_iterations.append(
                Attempt(
                    nodes[destination],
                    attempt.visited_nodes + [destination],
                    attempt.open_nodes + [current_node.name],
                    attempt.moves_left,
                    attempt.score,
                )
            )

    if len(attempt_iterations) == 0:
        # If there are no more productive moves for this iteration, mark it as done and put it back on the queue for score counting
        attempt.moves_left = 0
        attempt_iterations.append(attempt)
    # print(f"In visit node, just before reutning attmempt iterations: {attempt_iterations[0].score}")
    return attempt_iterations


def should_visit(potential_destination: str, attempt: Attempt, nodes: dict[str, Node]) -> bool:
    return True
    potential_destination_node = nodes[potential_destination]
    if len(potential_destination_node.tunnels) == 1 and potential_destination_node.flow_rate == 0:
        # Node doesn't lead anywhere, and it doesn't have any value ...
        return False
    ## This block broke the simple skip case for some reason ...
    if (
        len(potential_destination_node.tunnels) == 1
        and potential_destination_node.flow_rate > 0
        and potential_destination in attempt.visited_nodes
    ):
        # Node doesn't lead anywhere, and we already visited and didn't turn it on, shouldn't go back ..
        # In this scenario it would make sense to examine the node itself when we visited the first time and/or abort this particular
        return False
    if attempt.visited_nodes.count(potential_destination) > len(potential_destination_node.tunnels):
        # We've already been to this tunnel more times than it has branches, don't keep going back ...
        # May need to increase this to 2* node.tunnels to allow for some looping with eventual opening ...
        return False
    if (
        len(potential_destination_node.tunnels) == 2
        and len(attempt.visited_nodes) > 2
        and attempt.visited_nodes[-2] == potential_destination
    ):
        return False
    return True


def get_destination_nodes(attempt: Attempt, destinations: list[str], nodes: dict[str, Node]) -> list[str]:
    if len(destinations) == 1:
        # If there is only one possibility go there, regardless of visit count or open status
        return destinations
    else:
        d = [destination for destination in destinations if should_visit(destination, attempt, nodes)]
        return d


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        TOTAL_PRESSURE_RELEASED = process_list(input_file.readlines(), "AA", 26)
    print(f"Total pressure released: {TOTAL_PRESSURE_RELEASED}")
