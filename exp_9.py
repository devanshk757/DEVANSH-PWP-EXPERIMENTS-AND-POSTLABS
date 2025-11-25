# import pandas as pd
# data = [10, 20, 30, 44, 55]
# series = pd.Series(data)
# print(series)





# series2 = series + 10
# print(series2)
# filtered_series = series[series > 2]
# print(filtered_series)
# mean_value = series.mean()
# print(mean_value)







# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)
# print(df)




# # Accessing Columns (# select one column)
# print(df[['Name','Age']])




# # Adding a New Column
# df['Salary'] = [70000, 80000, 12000]
# print(df)





# # Dropping a Column
# df = df.drop('City', axis=1)
# print(df)





# # Return row 2:
# print(df.loc[[2]])








# #Return row 0 and 2:
# #use a list of indexes:
# print(df.loc[[0, 2]])










# import pandas as pd
# data = {
#   "calories": [120, 777, 2004],
#   "duration": [12, 77, 46]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)






# dat = pd.read_csv("data.csv")
# print(dat)





# Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
#         'Age': [28, 23, 35, 31],
#         'Gender': ['M', 'F', 'M', 'F']
#         }
# df = pd.DataFrame(Biodata)
# # Save the dataframe to a CSV file
# df.to_csv('Biodata.csv', index=False)









# dat = pd.read_csv("data.csv")
# print(dat.info())
# # shows first and last five rows
# print(dat.head())
# print(dat.tail())
# print(dat.describe())





# dat = pd.read_csv("data.csv")
# print(dat[['Name']])
# print(dat[['Name','Number']])
# print(dat.loc[[1]])




# import pandas as pd
# import numpy as np
# df = pd.DataFrame(
#     {
#     'A': [np.nan, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'B': np.random.normal(50, 15, 10),
#     'C': np.random.rand(10) * 100,
#     'D': np.linspace(1, 10, 10),
#     'E': np.logspace(1, 2, 10)
# }
# )
# print(df)








#postlab
#1
# import pandas as pd
# s1 = pd.Series([10, 20, 30, 40, 50])
# s2 = pd.Series([1, 2, 3, 4, 5])
# print("Addition:\n", s1 + s2)
# print("Subtraction:\n", s1 - s2)
# print("Multiplication:\n", s1 * s2)
# print("Division:\n", s1 / s2)





#2
# import pandas as pd
# data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# s = pd.Series(data)
# print(s)






#3
# import pandas as pd
# import numpy as np
# list_data = [10, 20, 30, 40]
# s1 = pd.Series(list_data)
# print("Series from List:\n", s1, "\n")
# array_data = np.array([100, 200, 300, 400])
# s2 = pd.Series(array_data)
# print("Series from NumPy Array:\n", s2, "\n")
# dict_data = {'a': 1, 'b': 2, 'c': 3}
# s3 = pd.Series(dict_data)
# print("Series from Dictionary:\n", s3)









#4
import pandas as pd
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])
vertical = pd.concat([s1, s2])
print("Vertical Stack:\n", vertical, "\n")
horizontal = pd.concat([s1, s2], axis=1)
print("Horizontal Stack:\n", horizontal)
