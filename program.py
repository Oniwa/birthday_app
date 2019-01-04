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

days_alive = todays_date - date_of_birth
print(delta_birth_date.days)

print(f'It looks like you were born on {date_of_birth.strftime("%m/%d/%Y")}')
