import day_07.puzzle_01.solution as s

PJTS_SIZE = 55644
RVS_SIZE = 16144
SWNGFRSJ_SIZE = 50956

CMWRQ_SIZE = RVS_SIZE + SWNGFRSJ_SIZE
ROOT_SIZE = CMWRQ_SIZE + PJTS_SIZE
COMMANDS = [
    "$ cd /",
    "$ ls",
    "dir cmwrq",
    "dir mddr",
    "dir mthvntdd",
    f"{PJTS_SIZE} pjts.dzh",
    "$ cd cmwrq",
    "$ ls",
    "dir dtbzzl",
    "dir pjnghbm",
    f"{RVS_SIZE} rvs",
    f"{SWNGFRSJ_SIZE} swngfrsj.pcj",
    "dir vhvn",
    "dir vrt",
    "dir zgrjmtcq"]

def test_basic_happy_path():
    assert s.find_total_size_of_dirs_under_threshold(COMMANDS, 1000000) == ROOT_SIZE + CMWRQ_SIZE

def test_only_one_directory_qualifies():
    assert s.find_total_size_of_dirs_under_threshold(COMMANDS, 68000) == CMWRQ_SIZE
