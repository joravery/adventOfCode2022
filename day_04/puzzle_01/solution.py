def process_spaces(cleaning_assignments: list):
    '''
    Comapres a pair of space cleaning assignments (Hyphenated string representing a range) and counts how many
    are subsets
    '''
    total_subsets = 0
    for assignment_pair in cleaning_assignments:
        [assignment_1, assignment_2] = assignment_pair.split(',')
        if is_sub_set(assignment_1, assignment_2):
            total_subsets += 1
    print(f"Total subsets: {total_subsets}")

def is_sub_set(range_1, range_2):
    '''
    Looks for subsets between two ranges
    '''
    # Could maybe create ranges or sets and do set arithmetic here ...
    [range_1_start, range_1_end] = [int(x) for x in range_1.split("-")]
    [range_2_start, range_2_end] = [int(x) for x in range_2.split("-")]
    if range_1_start <= range_2_start and range_1_end >= range_2_end:
        return True
    if range_1_start >= range_2_start and range_1_end <= range_2_end:
        return True
    return False

if __name__ == "__main__":
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_spaces(input_file.readlines())
