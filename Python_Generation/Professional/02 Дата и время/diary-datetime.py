from datetime import datetime

with open('diary.txt', 'r', encoding='UTF-8') as file:

    diary = sorted(file.read().split('\n\n'),
                   key=lambda x: datetime.strptime(x[:17], '%d.%m.%Y; %H:%M'))

print(*diary, sep='\n\n')