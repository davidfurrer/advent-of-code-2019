def is_increasing(x: int):
    x = list(str(x))

    valid = 0
    for i in range(1, len(x)):
        if x[i] >= x[i - 1]:
            valid += 1
    if valid == 5:
        return True
    else:
        return False


def is_valid(x: int):
    condition1 = len(str(x)) == 6
    condition2 = len(set(list(str(x)))) < 6
    condition3 = is_increasing(x)
    if condition1 & condition2 & condition3:
        return True
    else:
        return False


result = 0
for i in range(372037, 905157 + 1):
    if is_valid(i):
        result += 1


assert is_valid(111111) == True
assert is_valid(223450) == False
assert is_valid(123789) == False

print(result)
