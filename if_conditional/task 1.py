year_of_birth = int(input("Please enter your year of birth (e.g. 2000):"))

if year_of_birth < 1946:
    generation = "Silent Generation"
elif year_of_birth < 1965:
    generation = "Baby Boomer"
elif year_of_birth < 1981:
    generation = "Generation X"
elif year_of_birth < 1997:
    generation = "Millenials"
elif year_of_birth < 2012:
    generation = "Generation Z"
else:
    generation = "Generation Alpha"

print(f"You belong to: {generation}")