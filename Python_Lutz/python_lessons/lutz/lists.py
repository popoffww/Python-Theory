bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 50000, 'hardware']
people = [bob, sue]
for person in people:
    print(person)

for person in people:                                     # print(person[2]*1.20) - непонятно
    print(person[0].split()[1] + ' ', end='')
    print(person[2]*1.20)

pays = [person[2] for person in people]
sum = sum(person[2] for person in people)
print(pays, sum)

people.append(['Vitaly Popov', 44, 8000, 'osimchaim'])
print(people)
print(people[-1][0].split()[0] + ', Вы - нищий.')

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1],person[2][1])






