import pandas as pd
import tqdm

df = pd.read_csv("day2/input.txt", header=None).T
df.columns = ["p"]
pl = df.p.tolist().copy()

# 0 = add
# 1 = multiply
# 99 = stop

pl[1] = 12
pl[2] = 2


def run_program(im, jm):
    pl[1] = im
    pl[2] = jm
    for i, j in enumerate(pl):
        if i % 4 == 0:
            if j == 1:
                ii_ = pl[i + 3]
                pl[ii_] = pl[pl[i + 1]] + pl[pl[i + 2]]
            elif j == 2:
                ii_ = pl[i + 3]
                pl[ii_] = pl[pl[i + 1]] * pl[pl[i + 2]]
            else:
                return pl[0]
    return pl[0]


print("result part1:", run_program(12, 2))

result = 19690720
for ii in tqdm.tqdm(range(100)):
    for jj in range(100):
        pl = df.p.tolist().copy()
        result_ = run_program(ii, jj)
        if result == result_:
            r = 100 * ii + jj
            print("result part2:", r)
            break

