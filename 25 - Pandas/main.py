import pandas

data = pandas.read_csv("2018_Squirrel_Data.csv")
colors = ["Gray", "Cinnamon", "Black"]
g = 0
c = 0
b = 0

for color in range(1, len(data)):
    if data["Primary Fur Color"][color] == colors[0]:
        g += 1
    elif data["Primary Fur Color"][color] == colors[1]:
        c += 1
    else:
        b += 1

print(f"{colors[0]} = {g}")
print(f"{colors[1]} = {c}")
print(f"{colors[2]} = {b}")
