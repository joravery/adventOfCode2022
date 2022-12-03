def process_rucks(rucks: list):
    '''
    Rucksacks occur as a list of characters, one rucksack per line.
    Each rucksuck has two compartments, the first being the first half of the string and the second being the second.
    '''
    total = 0
    for i in range(0,len(rucks), 3):
        group_badge = get_group_badge([rucks[i], rucks[i+1], rucks[i+2]])
        total += get_value(group_badge)
    print(f"Total: {total}")

def get_group_badge(rucks: list):
    '''
    Finds the only item (character) that occurs in all three rucksacks (strings)
    '''
    smallest_ruck = sorted(rucks, key = lambda x: len(x), reverse=False)[0]
    print(f"smallest_ruck: {smallest_ruck}, rucks: {rucks}")
    for item in smallest_ruck:
        if item in rucks[0] and item in rucks[1] and item in rucks[2]:
            return item

def get_value(item:str):
    '''
    Returns the value of each item. Items (a-z) are valued 1-26 and items (A-Z) are valued 27-52
    '''
    if item.isupper():
        return ord(item)-38
    return ord(item)-96

if __name__ == "__main__":
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_rucks(input_file.readlines())