doggo_age_human = int(input(f"Enter the dog's age in human years:"))
doggo_years = float(0)
for doggo_age_human in range(1,doggo_age_human + 1):
    if doggo_age_human < 3:
        doggo_years += 10.5
    elif doggo_age_human >= 3:
        doggo_years += 4
doggo_years = int(doggo_years)
print(f"The dog's age in dog's years is {doggo_years} years")