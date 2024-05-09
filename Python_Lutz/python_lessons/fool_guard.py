bad_words = ['мудак','чмо','падло']
mes = 'Ты - мудак.'
if any(map(lambda x: x in bad_words, mes.split())):
    print('Бан')