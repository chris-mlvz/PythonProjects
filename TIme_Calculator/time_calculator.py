def add_time(start, duration, *day_week):

    # ! Variables
    list_start = []
    list_duration = []
    minutes_start = int()
    minutes_duration = int()
    minutes_end = int()
    minutes_changing = int()
    days = 0
    hours = 0
    minutes = 0
    format_hour = str()
    formats = ('AM', 'PM')
    MINUTES_24HOURS = 1440
    MINUTES_12HOURS = 720
    MINUTES_1HOUR = 60
    minutes_print = str()
    comment = str()
    day_week_print = str()
    TUPPLE_WEEK = ('monday', 'tuesday', 'wednesday',
                   'tuersay', 'friday', 'saturday', 'sunday')

    # ! Main
    # Data in lists
    list_start = start.split()
    list_start += (list_start[0].split(":"))
    list_duration = duration.split(":")

    # Operations
    if list_start[1] == formats[1]:
        minutes_start = int(
            list_start[2]) * MINUTES_1HOUR + int(list_start[3]) + MINUTES_12HOURS
    elif list_start[1] == formats[0]:
        minutes_start = int(list_start[2]) * MINUTES_1HOUR + int(list_start[3])

    minutes_duration = int(
        list_duration[0]) * MINUTES_1HOUR + int(list_duration[1])
    minutes_end = minutes_start + minutes_duration
    minutes_changing = minutes_end

    # # Output
    # print(list_start, list_duration)
    # print(minutes_start, minutes_duration, minutes_end)

    # Days
    if minutes_changing > MINUTES_24HOURS:
        days = int(minutes_changing / MINUTES_24HOURS)
        minutes_changing -= days * MINUTES_24HOURS
        if days == 1:
            comment = '(next day)'
        elif days > 1:
            comment = f'({days} days later)'
        # print(days)
        # print(minutes_changing)

    # Optional day of the week
    if day_week:
        day_week = day_week[0].lower()
        for i in range(len(TUPPLE_WEEK)):
            if day_week == TUPPLE_WEEK[i]:
                total_days = days + i
                while (total_days) >= 7:
                    total_days -= 7
                day_week_print = TUPPLE_WEEK[total_days]

    # PM
    if minutes_changing > MINUTES_12HOURS:
        minutes_changing -= MINUTES_12HOURS
        hours = int(minutes_changing / MINUTES_1HOUR)
        minutes = minutes_changing % MINUTES_1HOUR
        format_hour = formats[1]

    # AM
    elif minutes_changing < MINUTES_12HOURS:
        hours = int(minutes_changing / MINUTES_1HOUR)
        minutes = minutes_changing % MINUTES_1HOUR
        format_hour = formats[0]

    # 12 o'clock
    if hours < 1:
        hours += 12

    # format print
    if minutes < 10:
        minutes_print = f'0{minutes}'
    elif minutes >= 10:
        minutes_print = str(minutes)

    # end
    if day_week:
        new_time = f'{hours}:{minutes_print} {format_hour}, {day_week_print.capitalize()} {comment}'
    elif not day_week:
        new_time = f'{hours}:{minutes_print} {format_hour} {comment}'
    new_time = new_time.strip()
    return new_time


# actual = add_time("8:16 PM", "466:02", "tuesday")
# expected = "6:18 AM, Monday (20 days later)"
# print(actual)
# print(expected)
# if actual == expected:
#     print('si')
# else:
#     print('no')
