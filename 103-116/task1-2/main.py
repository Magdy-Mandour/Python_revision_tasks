#task1
#class game:
#    def __init__(self, name, developer, date, price):
#        self.name = name
#        self.developer = developer
#        self.date = date
#        self.price = price
#    def get_info(self):
#        pass
#game_one = game()
#task2
class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def full_details(self):
        print(f"hi my name is {self.first_name}")
user_one = User("magdy","mandour","34","male")
#user_two = User()
print(user_one.full_details())