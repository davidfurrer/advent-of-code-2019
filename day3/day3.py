import pandas as pd
import tqdm

df = pd.read_csv("day3/input.txt", header=None).T
df.columns = ["w1", "w2"]


x_c = 0
y_c = 0


def points_on_line(x1, y1, x2, y2):
    if y1 == y2:
        return [(x, y1) for x in range(x1, x2)]
    else:
        return [(x1, y) for y in range(y1, y2)]


print(points_on_line(2, 4, 34, 4))


def make_step(x, y, c):
    c1 = c[0]
    c2 = int(c[1:])
    if c1 == "R":
        x = x + c2
    elif c1 == "L":
        x = x - c2
    elif c1 == "D":
        y = y - c2
    else:
        y = y + c2
    return (x, y)


print(make_step(1, 3, "U4"))

points_visited = list()

for command in df.w1:
    x_c, y_c = make_step(x_c, y_c, command)
    points_visited.append((x_c, y_c))

print(points_visited)

additional_points = list()
for point1, point2 in zip(points_visited[:-1], points_visited[1:]):
    x1, y1 = point1
    x2, y2 = point2
    additional_points += points_on_line(x1, y1, x2, y2)


print(additional_points)



points_visited = list()
x_c = 0
y_c = 0
for command in df.w2:
    x_c, y_c = make_step(x_c, y_c, command)
    points_visited.append((x_c, y_c))

print(points_visited)

additional_points2 = list()
for point1, point2 in zip(points_visited[:-1], points_visited[1:]):
    x1, y1 = point1
    x2, y2 = point2
    additional_points2 += points_on_line(x1, y1, x2, y2)


intersection_points = list(set(additional_points) & set(additional_points2)) 
print(intersection_points)

d2 = 1000000000
for point in intersection_points:
    if (abs(point[0]) + abs(point[1])) < d2:
        d2 = (abs(point[0]) + abs(point[1]))

print(d2)


rd = 1000000000
for intersection_point in intersection_points:
    print(intersection_point)

    x_c = 0
    y_c = 0
    cs1 = 0
    for command in df.w1:
        print(command)
        x_c_, y_c_ = make_step(x_c, y_c, command)
        cs1 += abs(int(command[1:]))


    x_c = 0
    y_c = 0
    cs2 = 0
    while x_c != intersection_point[0]:
        for command in df.w2:
            (x_c, y_c) = make_step(x_c, y_c, command)
            cs2 += abs(int(command[1:]))
    if cs1 + cs2 < rd:
        rd = cs1 + cs2
        print(intersection_point)
        print(rd)

# todo 
