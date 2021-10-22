name = input("what's your name? ")
age =int(input("How old are you? "))
country = input("where are you from? ")
quots = '\ """"'
#print(f'"Hello \'{name.title()}\', How You Doing {quots} Your Age Is "{age}"" + Your Country Is: {country.title()}')
print(f'"Hello \'{name.title()}\', How You Doing \ \n{quots[1:-1]} Your Age Is "{age}"" + \nYour Country Is: {country.title()}')
