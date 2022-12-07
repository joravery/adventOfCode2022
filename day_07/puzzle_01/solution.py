from day_07.files import build_file_system

def find_total_size_of_dirs_under_threshold(lines: list, size_threshold: int):
    file_system_root = build_file_system(lines)
    return sum_dirs_less_than_size(file_system_root, size_threshold)

def sum_dirs_less_than_size(root, size_limit):
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