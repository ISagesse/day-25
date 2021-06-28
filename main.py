# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = csv.reader(data_file)
#     for temp in temperature:
#         print(temp[1])

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_average = data["temp"].to_list()
# average = sum(temp_average) / len(temp_average)
# print(round(average))

# print(data["temp"].mean())

# print(data["temp"].max()) getting the maximum value

# get Data in columns
# print(data["condition"])
# print(data.condition)

# get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# convert temperature from celsius to fahrenheit
# (C * 9/5) + 32 = F
# f_temp = (monday.temp * 9 / 5) + 32

# print(f_temp)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["amy", "James", "Israel"],
#     "scores": [76, 56, 65]
# }
# data_from_scratch = pandas.DataFrame(data_dict)
# print(data_from_scratch)
# data_from_scratch.to_csv("new_data.csv")