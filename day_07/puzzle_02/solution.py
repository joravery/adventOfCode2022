from day_07.files import build_file_system

def find_smallest_directory_to_obtain_required_space(lines: list, disk_size: int, space_required):
    file_system_root = build_file_system(lines)
    size_needed = space_required - (disk_size - file_system_root.size)
    print(f"Size required: {size_needed}")
    return min(find_dirs_greater_than_threshold(file_system_root, size_needed))

def find_dirs_greater_than_threshold(root, size_threshold):
    total = []
    if root.size >= size_threshold:
        total.append(root.size)
    for child in root.children:
        total += find_dirs_greater_than_threshold(root.get_child(child), size_threshold)
    return total

if __name__ == "__main__":
    DISK_SIZE = 70000000
    FREE_SPACE_REQUIRED = 30000000
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        smallest_directory = find_smallest_directory_to_obtain_required_space(input_file.readlines(), DISK_SIZE, FREE_SPACE_REQUIRED)
    print(f"Smallest directory over the required amount: {smallest_directory}")