class Num:
    """
    Simple class to disabmiguate duplicates in the list
    """

    def __init__(self, number) -> None:
        self.value = number


def process_list(lines: list):
    original = list()
    for line in lines:
        original.append(Num(int(line) * 811589153))
    new = list(original)
    for _ in range(10):
        for number in original:
            move_number(number, new)
    zero_index = [i for i in range(0, len(new)) if new[i].value == 0][0]

    return (
        new[(zero_index + 1000) % len(new)].value
        + new[(zero_index + 2000) % len(new)].value
        + new[(zero_index + 3000) % len(new)].value
    )


def move_number(number: Num, new_list: list[Num]):
    # print(f"new: {new_list}, processing number: {number}")
    current_index = new_list.index(number)
    new_index = (current_index + number.value) % (len(new_list) - 1)

    new_list.pop(current_index)
    new_list.insert(new_index, number)


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        answer = process_list(input_file.readlines())
    print(f"Answer: {answer}")
