import pandas as pd


df = pd.read_csv("day1/input.txt", names=["mass"])


def get_fuel_required(x):
    return int(x / 3) - 2


df["fuel_required"] = df["mass"].apply(lambda x: get_fuel_required(x))

total_fuel_required = df["fuel_required"].sum()
print(f"Part 1: {total_fuel_required}")


additional_fuel = 0
for fuel in df["fuel_required"]:
    fuel_ = fuel
    while get_fuel_required(fuel_) > 0:
        additional_fuel += get_fuel_required(fuel_)
        fuel_ = get_fuel_required(fuel_)


print(f"Part 2: {total_fuel_required + additional_fuel}")

