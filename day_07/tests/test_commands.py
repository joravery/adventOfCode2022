from day_07.commands import execute_cd, process_ls_output, parse_command
from day_07.node import Node

def test_process_ls_command():
    command = "$ ls"
    assert parse_command(command) == ("ls", None)

def test_process_cd_command():
    command = "$ cd foo"
    assert parse_command(command) == ("cd", "foo")

def test_first_directory_change():
    cwd = []
    destination = "/"
    execute_cd(destination, cwd)
    assert len(cwd) == 1
    assert cwd[0].name == destination

def test_add_directory():
    existing_name = "/"
    existing_node = Node(existing_name)
    new_destination = "new_dir"
    existing_node.add_child(new_destination)
    cwd = [existing_node]

    execute_cd(new_destination, cwd)
    assert len(cwd) == 2
    assert cwd[0].name == existing_name
    assert cwd[1].name == new_destination

def test_moving_up_a_dir():
    first_name = "/"
    existing_node = Node(first_name)
    new_destination = "new_dir"
    existing_node.add_child(new_destination)
    cwd = [existing_node]

    execute_cd(new_destination, cwd)
    execute_cd("..", cwd)

    assert len(cwd) == 1
    assert cwd[0].name == first_name

def test_process_ls_output_new_dir():
    cwd = []
    destination = "/"
    execute_cd(destination, cwd)
    process_ls_output("dir foo", cwd)
    assert "foo" in cwd[0].children

def test_process_ls_output_new_file():
    cwd = []
    destination = "/"
    execute_cd(destination, cwd)
    process_ls_output("12345 foo.txt", cwd)
    assert "foo.txt" in cwd[0].files
    assert cwd[0].files["foo.txt"] == 12345
    assert cwd[0].size == 12345
