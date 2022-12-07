from day_07.node import Node

def test_new_node():
    node = Node("/")
    assert node.name == "/"

def test_missing_child_node():
    node = Node("/")
    child_dir_name = "child_dir"
    assert child_dir_name not in node.children
    assert node.get_child(child_dir_name) is None


def test_add_new_child_dir():
    node = Node("/")
    child_dir_name = "child_dir"
    node.add_child(child_dir_name)
    assert child_dir_name in node.children
    assert isinstance(node.get_child(child_dir_name), Node)
    assert node.get_child(child_dir_name).name == child_dir_name

def test_add_new_file():
    node = Node("/")
    file_name = "foo.txt"
    file_size = 22
    assert node.size == 0
    node.add_file(file_name, file_size)
    assert file_name in node.files
    assert node.size == file_size
