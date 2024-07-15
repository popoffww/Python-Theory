def greet(name, owner):

    if name == owner:
        return f'Hello boss'
    return f'Hello guest'

    return "Hello boss" if name == owner else "Hello guest"

print(greet('Daniel', 'Daniel'), 'Hello boss')
print(greet('Greg', 'Daniel'), 'Hello guest')