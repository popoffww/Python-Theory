bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'soft'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 50000, 'job': 'hard'}
people = [bob, sue]
for person in people:
    print(person, '\t', people[bob][sue])

# list(map((lambda x: x['name']),people))