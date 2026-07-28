
class User:
    def __init__(self, name, money,user_id):
        self.id=user_id
        self.name = name
        self.money = money
        self.followers=0
        self.following=0
    def AumentarSeguidores(self,user):
        user.followers+=1
        self.following+=1


user_1 = User("juan",200,2)
user_2 = User("ana",400,3)

user_1.id=1
user_2.id=2

print(user_1.name, user_1.money,user_1.id)
print(user_2.name, user_2.money)

user_1.AumentarSeguidores(user_2)
print(user_1.followers, user_1.following)


