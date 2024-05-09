
print('\tУгадайте цвет (RGB-CMY) с пяти попыток.')
print("\tДля завершения напишите - 'выход'.")
max_attempt = 5
attempt = 0
color = 'cyan'
# for i in range(0,5): вариант с циклом for
while attempt < max_attempt:
    attempt += 1
    user_color = input('\tПопытка номер {}: '.format(attempt))
    if attempt == max_attempt:
        print('\tСегодня не Ваш день.')
        break
    if user_color == 'выход':
        print('\tОчень жаль. \n\tДо свидания!')
        break
    elif user_color != color:
        continue
    else:
        print('\tУгадали с {}'.format(attempt) + '-ой попытки.')
        break
print('\tИгра окончена.')



