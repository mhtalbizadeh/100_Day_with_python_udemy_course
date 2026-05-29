import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_+=[]{};:'\",.<>/?\\|`~"

password_list = []

print("hello welcome py password!")

nr_letters = int(input("how many letters would you like in your password ?"))
nr_numbers = int(input("how many numbers would you like in your password ?"))
nr_symbols = int(input("how many symbols would you like in your password ?"))

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))  

random.shuffle(password_list)
password = "".join(password_list)

print(f"your password is : {password}")