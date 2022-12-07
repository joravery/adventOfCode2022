from day_07.files import build_file_system

def test_process_ls_command():
    commands = [
        "$ cd /",
        "$ ls",
        "dir cmwrq",
        "dir mddr",
        "dir mthvntdd",
        "55644 pjts.dzh",
        "$ cd cmwrq",
        "$ ls",
        "dir dtbzzl",
        "dir pjnghbm",
        "16144 rvs",
        "50956 swngfrsj.pcj",
        "dir vhvn",
        "dir vrt",
        "dir zgrjmtcq"]
    root = build_file_system(commands)
    assert root.size == 55644 + 16144 + 50956
    assert len(root.children) == 3
    assert root.get_child("cmwrq").size == 16144 + 50956
    assert len(root.get_child("cmwrq").children) == 5
