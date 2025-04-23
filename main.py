
from datetime import datetime
date = "2020-10-09"



def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        current_day = datetime.now().date()
        return (current_day - date).days
    except ValueError:
        return 0
print(get_days_from_today(date))