# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(row)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

avg_temp = sum(temp_list) / len(temp_list)
data["temp"].mean()
print(avg_temp)

print(data_dict)