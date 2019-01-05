import datetime


def print_header():
    print('-------------------------------------------')
    print('              BIRTHDAY APP')
    print('-------------------------------------------')
    print()


def get_birthday_from_user():
    date_of_birth = input('When were you born [MM/DD/YYYY]? ')

    date_of_birth = date_of_birth.split('/')

    birth_date = datetime.date(year=int(date_of_birth[2]),
                                   month=int(date_of_birth[0]),
                                   day=int(date_of_birth[1]))

    print(f'It looks like you were born on {birth_date.strftime("%m/%d/%Y")}')

    return birth_date


def compute_days_until_birthday(birth_date):
    todays_date = datetime.date.today()

    years_alive = todays_date.year - birth_date.year

    if todays_date.month == birth_date.month:
        if todays_date.day == birth_date.day:
            days_until_birthday = birth_date - todays_date
        elif todays_date.day < birth_date.day:
            days_until_birthday = birth_date.replace(
                year=todays_date.year) - todays_date
        else:
            days_until_birthday = birth_date.replace(
                year=(todays_date.year + 1)) - todays_date
    elif todays_date.month < birth_date.month:
        days_until_birthday = birth_date.replace(
            year=todays_date.year) - todays_date
    else:
        days_until_birthday = birth_date.replace(
            year=todays_date.year + 1) - todays_date

    return days_until_birthday, years_alive


def print_birthday_info(days_until_birthday, years_alive):
    if days_until_birthday.days > 0:
        print(f'Looks like your birthday is in {days_until_birthday.days} days.'
              f'\nHope you\'re looking forward to it!')
    else:
        print(f'Happy Birthday!  You\'ve been on this planet for '
              f'{years_alive} years!')


def main():
    print_header()
    bday = get_birthday_from_user()
    number_of_days, days_alive = compute_days_until_birthday(bday)
    print_birthday_info(number_of_days, days_alive)


if __name__ == "__main__":
    main()
