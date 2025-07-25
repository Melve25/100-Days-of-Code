# lines = []
# with open("weather_data.csv") as file:
#     for line in file.readlines():
#         lines.append(line)
#
# print(lines)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         for word in row:
#             if word.isdigit():
#                 temperature.append(int(word))
#
# print(temperature)
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())
# print(data.condition)

# print(data[data["temp"] == 14])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((monday.temp * 9/5) + 32)

# data_dict = {
#     "students": ["Any", "Max", "Ilia"],
#     "scores": [76, 56, 43]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data_dict = {}
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]

data_dict["Fur Color"] = ["Gray", "Black", "Cinnamon"]
data_dict["Count"] = [len(gray), len(black), len(cinnamon)]


# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("squirrel_count.csv")
# print(data_frame)


