import pandas as pd
import tqdm


df = pd.read_csv("input.txt", header=None, names=["c"])
df["l"] = [x.split(")")[0] for x in df["c"]]
df["r"] = [x.split(")")[1] for x in df["c"]]


b = df.r.tolist() + df.l.tolist()
u = set(b)


def get_parent(x: str) -> str:
    return df.loc[df.r == x, "l"].values[0]


def steps_to_center(x: str) -> int:
    n_steps = 0
    while x != "COM":
        x = get_parent(x)
        n_steps += 1
    return n_steps


total = 0
for e in tqdm.tqdm(u):
    total += steps_to_center(e)

print(total)

