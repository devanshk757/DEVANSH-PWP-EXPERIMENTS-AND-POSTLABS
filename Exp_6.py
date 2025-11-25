# x = 10
# if x > 5:
#     print("x is greater than 5")


# x = 10
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")


# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")




# age = 35
# if age >= 60:
#     print("You are a senior citizen.")
# elif age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a teenager.")



# num = 10
# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive but odd.")
# else:
#     print("The number is not positive.")




# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)



# x = 1
# while x <= 5:
#     print(x)
#     x += 1



# for x in range(1, 6):
#     if x == 3:
#         break
#     print(x)



# for x in range(1, 6):
#     if x == 3:
#         continue
#     print(x)



# for x in range(1, 6):
#     if x == 3:
#         pass
#     print(x)



# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))






# def add_numbers(a, b):
#     return a + b

# result = add_numbers(3, 5)
# print(result)



# add = lambda x, y: x + y
# print(add(3, 5))




# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))



# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)



# def generate_numbers():
#     for i in range(1, 6):
#         yield i

# for number in generate_numbers():
#     print(number)




# # postlab
# i = 1
# while i <= 100:
#     if i % 2 != 0:
#         print(i, end=" ")
#     i += 1


# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("Sum of natural numbers from 1 to", n, "is:", sum)



# def count_digits(number):
#     count = 0
#     while number != 0:
#         number //= 10
#         count += 1
#     return count

# num = int(input("Enter a number: "))
# print("Number of digits:", count_digits(num))




# num = int(input("Enter a number: "))
# last_digit = num % 10

# first_digit = num
# while first_digit >= 10:
#     first_digit //= 10

# print("First digit:", first_digit)
# print("Last digit:", last_digit)



# num = input("Enter a number: ")

# if len(num) == 1:
#     swapped = num
# else:
#     swapped = num[-1] + num[1:-1] + num[0]

# print("Number after swapping first and last digits:", swapped)




# num = int(input("Enter a number: "))
# product = 1
# while num > 0:
#     digit = num % 10
#     product *= digit
#     num //= 10
# print("Product of digits:", product)




num = int(input("Enter a number: "))
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)
