
#1
# # # create a string using double quotes
# string1 = "Devansh Karia"
# print(string1)
# # create a string using single quotes
# string1 = ' 92510133006 '
# print(string1)



# #2
# string2 = 'Devansh'
# # access 1st index element
# print(string2 [1])




# #3
# string3 = 'Devansh'
# # access 4th last element
# print(string3 [-4]) 






# #4
# string4 = 'Devansh Karia'
# # access character from 1st index to 3rd index
# print(string4[1:4])  
# print(string4[:2])
# print(string4[2:])



# #5
# message = 'ICT Department'
# message[0] = 'H'
# print(message)


# message = 'ICT'
# # assign new string to message variable
# message = 'Devansh Karia'
# print(message)





# # multiline string 
# message = """
# Devansh Karia
# 92510133006
# """
# print(message)





# str1 = "Devansh"
# str2 = "Karia"
# str3 = "3EK1"
# print(str1 == str2)
# print(str1 == str3)




# greet = "Devansh"
# name = "Karia"
# # using + operator
# result = greet + name
# print(result)






# greet = 'Devansh'
# # count length of greet string
# print(len(greet))



# message = 'my name is devansh karia'
# # convert message to uppercase
# print(message.upper())





# message = 'MY NAME IS DEVANSH KARIA'
# # convert message to lowercase
# print(message.lower())



# text = 'CE Department'
# replaced_text = text.replace('CE', 'ICT')
# print(replaced_text)





# message = 'My name is Devansh Karia'
# # check the index of 'fun'
# print(message.find('Karia'))




# title = 'Devansh Karia  '
# result = title.rstrip()
# print(result)




# text = 'Devansh Karia'
# # split the text from space
# print(text.split())




# message = 'Devansh Karia'
# # check if the message starts with Python
# print(message.startswith('Karia'))





# pin = "07102006"
# # checks if every character of pin is numeric 
# print(pin.isnumeric())





# text = 'Python is fun'
# # find the index of is
# result = text.index('is')
# print(result)



# name = 'Devansh'
# country = 'India'
# print(f'{name} is from {country}')




# str = "This is a \n normal string example" 
# print(str) 
# raw_str = r"This is a \n raw string example" 
# print(raw_str)








# #1
# s = input("Enter a string: ")
# print(s[::-1])





#2
# s = input("Enter a string: ")
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")





#3
# s = input("Enter a string: ")
# if s.isdigit():
#     print("Only digits")
# else:
#     print("Contains non-digit characters")



#4
# s = input("Enter a sentence: ")
# words = s.split()
# longest = max(words, key=len)
# print("Longest word:", longest)



#5
s = input("Enter a sentence: ")
words = s.split()
print("Length of last word:", len(words[-1]))

