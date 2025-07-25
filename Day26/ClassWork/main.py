import pandas
# number = [1, 2, 3]
# new_list = [n + 1 for n in number]
# print(new_list)

# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# Ex_1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# Ex_2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# Ex_3
# with open("file1.txt") as f1:
#     file1 = f1.readlines()
# with open("file2.txt") as f2:
#     file2 = f2.readlines()
# # if in files we read at the last line we have "\n" - so extra empty line
# r = [int(num) for num in file1 if num in file2]
#
# # if in files we read at the last line we don't have "\n" - so no extra empty line
# list1 = [int(num.strip("\n")) for num in file1]
# list2 = [int(num.strip("\n")) for num in file2]
#
# result = [num1 for num1 in list1 if [num2 for num2 in list2 if num1 == num2]]
#
# print(r)
# print(result)

# Ex_4
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split(" ")}
# print(result)

# Ex_5
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {key: ((value * 9/5) + 32) for (key, value) in weather_c.items()}
#
# print(weather_f)

# student_dict = {
#     "student": ["Max", "Ilia", "Roman"],
#     "score": [56, 76, 98]
# }
# student_data = pandas.DataFrame(student_dict)
#
# for (index, row) in student_data.iterrows():
#     print(index)
#     print(row.student)
#     print(row["student"])
