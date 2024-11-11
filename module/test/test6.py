from datetime import datetime
import pytz

def dateforamatter(date, timezone='Asia/Manila'):

    tz = pytz.timezone(timezone)

    aware_date = date.astimezone(tz)
    
    formatted_date = aware_date.strftime("%B %d, %Y, %I:%M:%S %p")

    return formatted_date


datetime_ngayon = datetime.now()

print(datetime_ngayon)



parse_time = dateforamatter(datetime_ngayon)

print(parse_time)



