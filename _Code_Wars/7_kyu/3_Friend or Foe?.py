def friend(x):

    return [name for name in x if len(name) == 4]
    return list(filter(lambda name: len(name) == 4, x))


print(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"])
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])