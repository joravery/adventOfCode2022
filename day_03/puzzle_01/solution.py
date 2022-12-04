def process_rucks(rucks: list):
    '''
    Rucksacks occur as a list of characters, one rucksack per line.
    Each rucksuck has two compartments, the first being the first half of the string and the second being the second.
    '''
    total = 0
    for ruck in rucks:
        duplicate = find_duplicate(ruck)
        total += get_value(duplicate)
    print(f"Total: {total}")

def get_value(item:str):
    '''
    Returns the value of each item. Items (a-z) are valued 1-26 and items (A-Z) are valued 27-52
    '''
    if item.isupper():
        return ord(item)-38
    return ord(item)-96

def find_duplicate(ruck):
    '''
    Returns the item (character) that occurs in both compartments of the rucksack (both halves of the string)
    '''
    ruck_size = len(ruck)
    second_compartment = ruck[int(ruck_size/2):]
    for i,item in enumerate(ruck):
        if i >= len(ruck)/2:
            return -1
        if item in second_compartment:
            return item

if __name__ == "__main__":
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_rucks(input_file.readlines())
