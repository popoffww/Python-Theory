# wicket={'1': 'Bowled', '2': 'Run Out', '3': 'Stumped', '4': 'Catch', '5': 'Caught & Bowled', '6': 'Leg Before Wicket'}
# print('Kind of wicket')
# for kind in wicket:
#     print(kind,':', wicket[kind])
# print(wicket.items())
#
# out = dict.fromkeys(['1', '2', '3'],['Bowled', 'Run Out', 'Stumped'])
# print(out)
#
# L = list(zip(['1', '2', '3'], ['Bowled', 'Run Out', 'Stumped']))
# print(L)
#
# d = dict(zip(['1', '2', '3'], ['Bowled', 'Run Out', 'Stumped']))
# print(d)
#
# D = dict(a='Bowled', b='Run Out', c='Stumped')
# print(D)
#
# DD = dict([(1,'Bowled'), ('2','Run Out'), ('c','Stumped')])
# print(DD)
#
# def cricket(*args, **kwargs):
#     print(args)
#     print(kwargs)
# cricket('a: Bowled','b: Run Out',c='Stumped')

bbl_cities = dict([(1, 'Adelaide'), (2, 'Brisbane'), (3, 'Melbourne'), (4, 'Perth')])
print(bbl_cities)
bbl_cities.setdefault('5', 'Sydney')
print(bbl_cities.keys())

derby_1 = dict.fromkeys(['Thunder','Sixers'], 'Sydney')
print(derby_1)
derby_2 = dict.fromkeys(['Renegades','Stars'],'Melbourne')
print(derby_2)