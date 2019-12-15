import pandas as pd


df = pd.read_csv("input.txt", header=None, names=["c"])
input_string = df["c"].values[0]

s = list(range(150, 15150, 150))


def get_num(x, n=0):
    return list(x).count(str(n))


layers = list()
layer_num = 0
num_zeros = 100000000
i_p = 0
best_layer = 0
best_string = ""

for i in s:
    layer_num += 1

    if get_num(input_string[i_p:i]) < num_zeros:
        num_zeros = get_num(input_string[i_p:i])
        best_layer = layer_num
        best_string = input_string[i_p:i]
    i_p = i

result = get_num(best_string, n=1) * get_num(best_string, n=2)



print(result)
