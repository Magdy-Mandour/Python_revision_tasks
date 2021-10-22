#task1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud","Emad","wael"]
print(friends[:1])
print(friends[0])
print(friends[-1])
print(friends.pop())
#end task1
#task 2
print(friends[1::2])
print(friends[::2]) #I dnt know why last elemtn not included?
#end task 2
#task3
print(friends[1:4])
print(friends[-2:]) #same problem again "wael" is not seen by python
#end task 3
#task4
new_friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud","Emad","wael"]
new_friends[-2] = "Elzero"
new_friends [-1] = "Elzero"
print(new_friends)
#end task 4
#task5
friends_task5 = ["Osama", "Ahmed", "Sayed"]
friends_task5.insert(0,"mandour")
friends_task5.append("magdy")
print(friends_task5)
#end task 5
#task6
new_friends_task6 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud","Emad","wael"]
del new_friends_task6[:2]
print(new_friends_task6)
new_list = ['Sayed', 'Ali', 'Mahmoud', 'Emad', 'wael']
new_list.pop(-1)
print(new_list)
#end task 6
#task 7
friends1 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
final_list = friends1 + employees + school
print(final_list)
#end task 7
#task 8
organized_friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
organized_friends.sort() 
print(organized_friends)
organized_friends.sort(reverse = True)
print(organized_friends)
#end task 8
#task 9
total_friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(total_friends))
#end task 
#task 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
#end task 10