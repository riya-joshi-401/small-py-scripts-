import random
import string

print("Welcome to Password Generator!")

length = int(input('\nEnter the length of the Password: '))
lower = string.ascii_lowercase  # Produces lower case letters
upper = string.ascii_uppercase  # Produces upper case letters
num = string.digits             # Produces numeric digit
symbols = string.punctuation    # Produces special characters

all = lower + upper + num + symbols

temp = random.sample(all, length)  # generate random numbers
password = "".join(temp)
print(password)
