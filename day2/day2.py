import pandas as pd

df = pd.read_csv("day2/input.txt", header=None).T
df.columns = ['p']
pl = df.p.tolist()

print(pl)
# 0 = add
# 1 = multiply
# 99 = stop

pl[1] = 12
pl[2] = 2


for i, j in enumerate(pl):
    print(i, j)
    if i % 4 == 0:
        print(i)
        if j == 1:
            ii = pl[i + 3]
            pl[ii] = pl[pl[i+1]] + pl[pl[i+2]]
        elif j == 2:
            ii = pl[i + 3]
            pl[ii] = pl[pl[i+1]] * pl[pl[i+2]]
        elif df.loc[i, "p"] == 99:
            print("break 99")
            break
        else:
            print("break unknown")
            break

print('result part1:', pl[0])