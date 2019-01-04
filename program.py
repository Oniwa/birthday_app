import datetime

print('-------------------------------------------')
print('              BIRTHDAY APP')
print('-------------------------------------------')

date_of_birth = input('When were you born [MM/DD/YYYY]? ')

date_of_birth = date_of_birth.split('/')

birth_date = datetime.datetime(year=int(date_of_birth[2]),
                               month=int(date_of_birth[0]),
                               day=int(date_of_birth[1]))

todays_date = datetime.datetime.now()

days_alive = todays_date - birth_date
print(days_alive.days)

print(f'It looks like you were born on {birth_date.strftime("%m/%d/%Y")}')
if todays_date.month == birth_date.month:
    if todays_date.day == birth_date.day:
        print(f'Happy Birthday!  You\'ve been on this planet for '
              f'{days_alive.days} days!')
    elif todays_date.day < birth_date.day:
        days_until_birthday = birth_date.replace(
            year=todays_date.year) - todays_date
        print(f'Looks like your birthday is in {days_until_birthday.days} days.')
        print('Hope you\'re looking forward to it!')
    else:
        days_until_birthday = birth_date.replace(
            year=(todays_date.year + 1)) - todays_date
        print(
            f'Looks like your birthday is in {days_until_birthday.days} days.')
        print('Hope you\'re looking forward to it!')
