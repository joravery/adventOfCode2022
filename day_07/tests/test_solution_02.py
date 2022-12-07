import day_07.puzzle_02.solution as s

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
    assert s.find_smallest_directory_to_obtain_required_space(COMMANDS, 150000, 50000) == CMWRQ_SIZE

def test_space_requires_deleting_root():
    assert s.find_smallest_directory_to_obtain_required_space(COMMANDS, 150000, 140000) == ROOT_SIZE
