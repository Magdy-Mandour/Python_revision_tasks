set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
if set_one.intersection(set_two):
    print(True)

# No Need For Condition 

set_one = {1, 2, 3}

set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))  # True
