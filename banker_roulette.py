
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names) - 1
random_name = random.randint(0,length)
bill_payer = names[random_name]
print(f"{bill_payer} is going to pay the bills")
