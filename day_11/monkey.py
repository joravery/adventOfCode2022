import math

class Monkey:
    def __init__(self, items: list, inspection_function: callable, test_function: callable, worry_reduction_function: callable):
        self.items = items
        self.inspect_operation = inspection_function
        self.test = test_function
        self.worry_reduction = worry_reduction_function
        self.inspection_count = 0

    def inspect_next_item(self):
        if len(self.items) == 0:
            raise ValueError("Should not call inspect on a monkey with no items ...")
        self.inspection_count += 1

        initial_worry_level = self.items.pop(0)
        total_worry = self.inspect_operation(initial_worry_level)
        total_worry = self.worry_reduction(total_worry)
        destination = self.test(total_worry)
        return (destination, total_worry)


    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def __gt__(self, other):
        return self.inspection_count > other.inspection_count

    def __lt__(self, other):
        return self.inspection_count < other.inspection_count

    def __eq__(self, other):
        return self.inspection_count == other.inspection_count
