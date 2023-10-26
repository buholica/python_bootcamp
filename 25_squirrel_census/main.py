import pandas

squirrel_data = pandas.read_csv("2018_Squirrel_Census.csv")
grey_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

grey_sq_amount = len(grey_squirrels)
red_sq_amount = len(red_squirrels)
black_sq_amount = len(black_squirrels)

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_sq_amount, red_sq_amount, black_sq_amount]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
print(new_data)
