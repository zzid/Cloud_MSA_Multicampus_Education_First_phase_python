##############################################
# This is my class file from same directory###
from class_oop import SoccerPlayer         ###
##############################################
temp = SoccerPlayer('David','DF', 3)
print(temp) ## __str__ function makes this happen well
# without __str__, it will print address
print(temp.__str__()) ## same with upper one
temp.change_back_number(5)



names = ['Jin','Sungchul', 'Ronaldo', 'Hong', 'Seo']
positions = ['MF', 'DF', 'CF', 'WF', 'GK']
numbers = [10,15,20,3,1]

players = [[name, position, number] for name, position, number in zip(names,positions,numbers)]
print(players)
players_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names,positions,numbers)]
for i in range(len(players_objects)):
    print(players_objects[i].introduce())

    