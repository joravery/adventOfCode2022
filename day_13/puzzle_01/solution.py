def process_list(lines: list):
    correct_signals = []
    for i in range(0, len(lines), 3):
        left_side = eval(lines[i])
        right_side = eval(lines[i+1])
        result = compare_sides(left_side, right_side)
        if result is True:
            correct_signals.append((i//3) + 1)
    print(correct_signals)
    return sum(correct_signals)


def compare_sides(left: list, right: list):
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] > right[i]:
                return False
            if left[i] < right[i]:
                return True
        elif isinstance(left[i], list) and isinstance(right[i], list):
            result = compare_sides(left[i], right[i])
            if result is not None:
                return result
        elif isinstance(left[i], int) and isinstance(right[i], list):
            result = compare_sides([left[i]], right[i])
            if result is not None:
                return result
        elif isinstance(left[i], list) and isinstance(right[i], int):
            result = compare_sides(left[i], [right[i]])
            if result is not None:
                return result
        i += 1
    if len(left) > len(right):
        return False
    if len(right) > len(left):
        return True
    return None


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        s = process_list(input_file.readlines())
    print(s)
