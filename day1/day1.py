import pandas as pd


df = pd.read_csv("day1/input.txt", names=["mass"])


def get_fuel_required(x):
    return int(x / 3) - 2


df["fuel_required"] = df["mass"].apply(lambda x: get_fuel_required(x))

total_fuel_required = df["fuel_required"].sum()
print(total_fuel_required)
