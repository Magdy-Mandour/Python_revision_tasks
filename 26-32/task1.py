first_list = [1,2,3,3,4,5,1]
unique_list = set(first_list)
print(unique_list)
final_list = list(unique_list)
print(type(final_list))
final_list.pop()
print(final_list)