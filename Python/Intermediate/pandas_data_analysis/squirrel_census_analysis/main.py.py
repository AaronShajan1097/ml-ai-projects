import pandas as pd

data = pd.read_csv("/data/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

total_gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
total_cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
total_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

new_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [total_gray_squirrels, total_cinnamon_squirrels, total_black_squirrels]
}

df = pd.DataFrame(new_data)
df.to_csv("squirrel_count.csv")
