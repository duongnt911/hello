import random
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
year = year_of_birth + random.randint(0,70)
print(f"Hello {name}, your lucky year is {year}")

print()
input("Press return to continue ...")