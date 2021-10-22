#task6
num = input("Enter a number: ")
def return_zero(num):
    if len(num) == 4:
        return num
    elif len(num)== 3:
        return f"0{num}"
    elif len(num)== 2:
        return f"00{num}"
    elif len(num)== 1:
        return f"000{num}"
print(return_zero(num))
#end task 6
#task7
name = input("Enter your name ")
added_symbol = "@"
standard = 20 
symbol_number = standard - len(name)
desired_symbol =  symbol_number * "@"
print(f"{desired_symbol}{name}")
#end task 7
#task 8
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())