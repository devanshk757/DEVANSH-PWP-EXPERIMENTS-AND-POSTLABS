# import matplotlib.pyplot as plt 
# x = [3, 1, 3] 
# y = [3, 2, 1] 
# plt.plot(x, y)
# plt.title("Line Chart")
# plt.legend(["Line"])
# plt.show()





# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0.1, 2 * np.pi, 41)
# y = np.exp(np.sin(x))
# plt.stem(x, y)  
# plt.title("Stem Plot")
# plt.show()








# import matplotlib.pyplot as plt 
# x = [3, 1, 3, 12, 2, 4, 4] 
# y = [3, 2, 1, 4, 5, 6, 7] 
# plt.bar(x, y)
# plt.title("Bar Chart")
# plt.legend(["bar"])
# plt.show()





# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4, 5, 6, 7, 4] 
# plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
# plt.title("Histogram")
# plt.legend(["bar"])
# plt.show()





# import matplotlib.pyplot as plt 
# x = [3, 1, 3, 12, 2, 4, 4]
# y = [3, 2, 1, 4, 5, 6, 7]
# plt.scatter(x, y)
# plt.legend("A")
# plt.title("Scatter chart")
# plt.show()





# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(10)
# data = np.random.normal(100, 20, 200)
# fig = plt.figure(figsize =(10, 7))
# plt.boxplot(data)
# plt.show()










# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4] 
# e  =(0.1, 0, 0, 0)
# plt.pie(x, explode = e)
# plt.title("Pie chart")
# plt.show()






# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 2, 1, 2, 1, 2, 1]
# y_error = 0.2  
# plt.plot(x, y)  
# plt.errorbar(x, y, yerr=y_error, fmt='o')
# plt.show()




# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# z = [1, 8, 27, 64, 125]
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot3D(z, y, x)
# plt.show()





#post lab
#1
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.xlabel("X Axis Label")
# plt.ylabel("Y Axis Label")
# plt.title("Simple Line Chart")
# plt.show()








#2
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y1 = [1, 2, 3, 4, 5]        
# y2 = [1, 4, 9, 16, 25]      
# y3 = [1, 8, 27, 64, 125]    
# plt.plot(x, y1, label="y = x")          
# plt.plot(x, y2, label="y = x²")        
# plt.plot(x, y3, label="y = x³")        
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("Multiple Line Graph Example")
# plt.legend()   
# plt.show()








#3
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]        
y2 = [1, 4, 9, 16, 25]     
y3 = [1, 8, 27, 64, 125]   
plt.plot(x, y1, label="y = x")          
plt.plot(x, y2, label="y = x²")        
plt.plot(x, y3, label="y = x³")         
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple Line Graph Example")
plt.legend()   
plt.show()
