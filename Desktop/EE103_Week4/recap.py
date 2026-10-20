std_num_str = input("Please enter your student number")
std_num = int(std_num_str)
print(f"Hello! my student number is {std_num}")

name_lower = 'name'
name_upper = name_lower.upper()
name_reversed = name_lower[:: -1]

this_year = 2026
this_year_str = str(this_year)
first_two = float(this_year_str[:2])
last_two = float(this_year_str[2:])

mysum = first_two + last_two
print(f"{mysum:.2f}")

if mysum == 46:
    print("Correct")
else:
    print("Wrong")