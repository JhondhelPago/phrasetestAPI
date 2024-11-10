from datetime import datetime

def dateforamatter(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_date = date.strftime("%B %d, %Y, %I:%M:%S %p")

    return formatted_date

value = dateforamatter('2024-11-10T02:50:44.853421Z')
print(value)



