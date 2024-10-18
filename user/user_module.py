import random
from datetime import datetime

def otp_generator():

    return random.randint(100000, 999999)

# time_string parameter format should be: "2024-10-17 23:26:52.498729"
def time_dissect(time_string):

    date_time_list = time_string.split(' ')

    date_string = date_time_list[0]
    time_string = date_time_list[1]

    date_list = date_string.split('-')
    
    time_list = time_string.split(':')


    sec_milisec = time_list[-1].split('.')



    # return date_time_list + time_list[:len(time_list)] 

    formatTimeList = [date_list[0], date_list[1], date_list[2], time_list[0], time_list[1], sec_milisec[0], sec_milisec[1]]

    for i in range(len(formatTimeList)):

        formatTimeList[i] = int(formatTimeList[i])

    return formatTimeList

#this function return the seconds difference to two time instances
def time_difference(datetime1, datetime2):

    datetime1_param_list = time_dissect(datetime1)
    print(f"datetime1_param_list: {datetime1_param_list}")

    print(datetime2)
    datetime2_param_list = time_dissect(datetime2)
    print(f"datetime2_param_list: {datetime2_param_list}")

    datetime1_instance = datetime(
        datetime1_param_list[0],
        datetime1_param_list[1],
        datetime1_param_list[2],
        datetime1_param_list[3],
        datetime1_param_list[4],
        datetime1_param_list[5],
        datetime1_param_list[6]
    )


    datetime2_instance = datetime(
        datetime2_param_list[0],
        datetime2_param_list[1],
        datetime2_param_list[2],
        datetime2_param_list[3],
        datetime2_param_list[4],
        datetime2_param_list[5],
        datetime2_param_list[6],
    )


    time_dif_value = abs(datetime2_instance - datetime1_instance)


    return time_dif_value.total_seconds()


def time_dif_under2mins(datetime1, datetime2):

    seconds_diffrence = time_difference(datetime1, datetime2)
    print(f"seconds_difference: {seconds_diffrence}")

    if seconds_diffrence <= 240:

        return True
    
    else:

        return False
    
def removeUTC_symbol(datetimeObject):

    datetimeObject_string = str(datetimeObject)

    return datetimeObject_string.replace("+00:00", "")
    










