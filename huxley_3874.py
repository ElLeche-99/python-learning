def verify_prime(number):
    count = 0
    for prime in range(number):
       if (prime != 0 and prime != 1):
           if (number % prime == 0):
               count += 1
    return count


def verify_perfect_square(number):
    root = number ** 1/2
    if(isinstance(root, int)):
        return True
    else:
        return False
    
class User:
    def __init__(self, age, id_value, name):
        self.age = age
        self.id = id_value
        self.name = name
        self.points = 0

age_id_1 = input()
name_1 = input()
age_id_2 = input()
name_2 = input()


age_id_1 = age_id_1.split(' ')
age_id_2 = age_id_2.split(' ')


user_1 = User(int(age_id_1[0]), int(age_id_1[1]), name_1)
user_2 = User(int(age_id_2[0]), int(age_id_2[1]), name_2)

if(len(user_1.name) > len(user_2.name)):
    user_1.points += 2
elif(len(user_1.name) < len(user_2.name)):
    user_2.points += 2

if(verify_prime(user_1.age) == 1):
    user_1.points += 4
if(verify_prime(user_2.age) == 1):
    user_2.points += 4

if(verify_perfect_square(user_1.id)):
    user_1.points += 3

if(verify_perfect_square(user_2.id)):
    user_2.points += 3

if(user_1.points > user_2.points):
    print("{} WINS".format(user_1.name))
elif(user_2.points > user_1.points):
    print("{} WINS".format(user_2.name))
else:
    print("CInCABECAS EMPATADOS")
