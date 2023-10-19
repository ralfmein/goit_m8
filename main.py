from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    today = date.today()

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=7)

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    for user in users:
        name = user['name']
        birthday = user['birthday']
        print(name, birthday)
        birthday = birthday.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if start_of_week <= birthday <= end_of_week:
            day_of_week = birthday.strftime('%A')
            if day_of_week in birthdays_per_week:
                birthdays_per_week[day_of_week].append(name)
            else:
                birthdays_per_week['Monday'].append(name)

    birthdays_per_week = {key: value for key, value in birthdays_per_week.items() if value}
    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
