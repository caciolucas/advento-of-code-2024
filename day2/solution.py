levels = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        levels.append([int(n) for n in line.split(" ")])

safe_levels = 0


def check_safety(level):
    level_type = "increasing" if level[1] > level[0] else "decreasing"
    for i in range(len(level) - 1):
        difference = abs(level[i + 1] - level[i])
        if not (1 <= difference <= 3):
            return False
        elif level_type == "increasing" and level[i] > level[i + 1]:
            return False
        elif level_type == "decreasing" and level[i] < level[i + 1]:
            return False

    return True


for level in levels:
    if check_safety(level):
        safe_levels += 1

print(safe_levels)


safe_levels_with_problem_dumpener = 0


def check_safety_with_problem_dumpener(level):
    if check_safety(level):
        return True

    for i in range(len(level)):
        modified_level = level.copy()
        modified_level.pop(i)
        if check_safety(modified_level):
            return True
    return False


for level in levels:
    if check_safety_with_problem_dumpener(level):
        safe_levels_with_problem_dumpener += 1

print(safe_levels_with_problem_dumpener)
