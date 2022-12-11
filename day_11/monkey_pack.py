from functools import reduce
from day_11.monkey import Monkey


class MonkeyPack:
    def __init__(self, monkeys: list[Monkey]) -> None:
        self.monkeys = monkeys

    def execute_round(self):
        for monkey in self.monkeys:
            self.process_single_monkey(monkey)
        pass

    def process_single_monkey(self, monkey: Monkey):
        for _ in range(0, len(monkey.get_items())):
            destination, item = monkey.inspect_next_item()
            self.monkeys[destination].add_item(item)

    def get_n_active_monkeys(self, active_count=1):
        monkey_count = len(self.monkeys)
        if active_count > monkey_count:
            raise ValueError(
                f"Cannot return {active_count} most active monkeys with only {monkey_count} monkeys in the pack")
        return sorted(self.monkeys, reverse=True)[0:active_count]

    def monkey_business(self, active_count=1):
        top_monkeys = self.get_n_active_monkeys(active_count)
        mischief = [monkey.inspection_count for monkey in top_monkeys]
        return reduce((lambda x, y: x * y), mischief)
