from datetime import datetime, timedelta

def date_in_future(integer):
    time = (datetime.now()).time().replace(microsecond=0)
    date = datetime.now()

    if isinstance(integer, int):
        date += timedelta(days=integer)
        print(f"{date.strftime('%d.%m.%Y')} {time}")
    else:
        print(f"{date.strftime('%d.%m.%Y')} {time}")

date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня
