import math
#task2
x = 1+2j
print(x.imag)
print(x.real)
#end task 2
#task 3
num = 10
print(f"{num:.10f}")
#end task 3
#task4
num = int(159.650)
print(math.floor(num))
#end task 4
#task5
def calculations(num1,num2,result):
    if num1 + num2 == result:
        return "+"
    elif num1 - num2 == result:
        return "-"
    elif num1 * num2 == result:
        return "*"
    elif num1 / num2 == result:
        return "/"
    else:
        return "%"
print(calculations(97 , 20 , 4))
#end task 5