import sys

def find_first_unique_substring(signal: str, sub_string_length: int):
    '''
    Returns the end position of a character in a string using a 1-indexed system for character counting.
    '''
    for i in range(sub_string_length, len(signal)+1):
        if len(set(signal[i-sub_string_length:i])) == sub_string_length:
            return i
    return -1

if __name__ == "__main__":
    SUB_STRING_LENGTH = 4 if len(sys.argv) <2 else int(sys.argv[1])

    with open("../input.txt", "r", encoding="utf-8") as input_file:
        signal = input_file.readlines()[0]
        sub_string_end = find_first_unique_substring(signal, SUB_STRING_LENGTH)
        print(f"The first unique substring of size {SUB_STRING_LENGTH} is: '{signal[sub_string_end-SUB_STRING_LENGTH:sub_string_end]}\'")
        print(f"The substring end at the {sub_string_end+1}th position")
