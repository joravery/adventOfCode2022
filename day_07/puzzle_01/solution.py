from day_07.files import build_file_system

def find_total_size_of_dirs_under_threshold(lines: list, size_threshold: int):
    '''
    Builds a file system based on a list of CLI commands and output and then returns the sum of directories below the threshold
    '''
    file_system_root = build_file_system(lines)
    return sum_dirs_less_than_size(file_system_root, size_threshold)

def sum_dirs_less_than_size(root, size_limit):
    '''
    Recursively looks through the file system totaling the size of any directory below the size_limit.
    The behavior can lead to "double counting", which is as desired.
    '''
    total = 0
    if root.size <= size_limit:
        total += root.size
    for child in root.children:
        total += sum_dirs_less_than_size(root.get_child(child), size_limit)
    return total

if __name__ == "__main__":
    DIRECTORY_SIZE_THRESHOLD = 100000
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        total_dir_size = find_total_size_of_dirs_under_threshold(input_file.readlines(), DIRECTORY_SIZE_THRESHOLD)
    print(f"Total size of all directories under {DIRECTORY_SIZE_THRESHOLD}: {total_dir_size}")
