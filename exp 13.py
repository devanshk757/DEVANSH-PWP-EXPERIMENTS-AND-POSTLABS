file1 = open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt")

# f1 = open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt")
# # This will print every line one by one in the file
# for each in f1:
#     print (each)


# # Python code to illustrate read() mode
# f1 = open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt")
# print (f1.read())




# with open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt",'r') as f1:  
#     data = f1.read() 
# print(data)



# f1 = open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt")
# print (f1.read(5))




# with open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt",'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)




# file = open("ict1.txt",'w')
# file.write("ICT ICT ICT \n")
# file.write("ICT ICT ICT ICT ICT")
# file.close()

# with open("file.txt", "w") as f: 
#     f.write("Hello World!!!") 
#     f.close()





# file = open("ict1.txt",'a')
# file.write("\n Department Department")
# file.close()




# with open(r'D:\DEGREE SEM 3\PWP MS\EXP13\a.tif', 'rb') as file:
#     binary_data = file.read()
# with open('c.tif', 'wb') as f:
#     f.write(binary_data)
#     f.close()




# # Reading from a CSV file
# import csv
# with open('data-1.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)





# # Writing to a CSV file
# import csv
# with open('Output:-.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Subject', 'Mark'])
#     writer.writerow(['Devansh', 'PWP', 9])
#     writer.writerow(['Heet', 'PWP', 10])
#     file.close()



# import csv
# with open('Output:-.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Subject', 'Mark'])
#     writer.writerow(['Devansh', 'PWP', 9])
#     writer.writerow(['Heet', 'PWP', 10])
#     file.close()
# with open("Output:-.csv", "r") as f:
#     print(f.read())







#postlab
#1
# with open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt",'r') as f1:
#     text = f1.read()

# lines = text.splitlines()
# words = text.split()
# chars = len(text)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", chars)






#2
# with open(r"D:\DEGREE SEM 3\PWP MS\EXP13\ict.txt",'r') as f1:
#     lines = f1.readlines()

# lines = [line.strip() for line in lines]  # remove \n
# print(lines)




# import csv

# with open("data-1.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)







with open("ict.txt", "r") as f1, open("ict1.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as f3:
    f3.write(data1 + "\n" + data2)

print("Files merged successfully into merged.txt")
