import functools


def process_list(lines: list):
    signals = [eval(line) for line in lines if line != "\n"]
    signals.append([[2]])
    signals.append([[6]])
    print(signals)
    ssignals = sorted(signals, key=functools.cmp_to_key(
        lambda a, b: -1 if compare_sides(a, b) else 1))
    print((ssignals.index([[6]]) + 1) * (ssignals.index([[2]])+1))


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
