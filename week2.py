"""num_list = ['2','3','4']
print(num_list)

new_list = [ (int(num) + 1) for num in num_list ] # list comprehension, 
print(new_list)"""


"""from students import Student

student1 = Student('Alex', 'sdf165sd')
print(student1)"""

"""from dice import Dice # importing Dice from dice module

dice1 = Dice()
dice2 = Dice(10)

print(dice1.roll())
print(dice2.roll())"""

from students import Student # importing Student from students module

student1 = Student('Alex', 'sdf165sd', 3.8)
student2 = Student('Lee', 'sdf169sd', 3.2)
student3 = Student('Berry', 'sdf122sd', 2.8)

student1 = Student('Alex', 'sdf165sd', 3.65)

print(student1)
print(student2)
print(student3)




