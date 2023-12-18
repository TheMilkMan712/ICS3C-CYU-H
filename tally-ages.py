# Programmer: 
# Description: 

# Read a list of ages from a file into the variable ages
ages_file = open("ages.txt")
ages = [int(age) for age in ages_file]
ages_file.close()

voters = 0
non_voters = 0
for age in ages:
    if age >= 18:
        voters += 1
        
for age in ages:
    if age < 18:
        non_voters += 1

print(f"Voters: {voters}")
print(f"Non-Voters: {non_voters}")