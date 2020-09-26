def add_time(start, duration, day=''):
    startPos = start.find(':')
    durPos = duration.find(':')
    shours = start[:startPos]
    smin = start[startPos+1:startPos+3]
    dhours = duration[:durPos]
    dmin = duration[durPos+1:durPos+3]
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    s = 'AM'
    min = int(smin)+int(dmin)
    res = 0
    #print('min', min)
    if min > 60:
        min = min % 60
        #print(min, '00000')
        res = 1
    hours = int(shours) + int(dhours) + res
    days = 0
    #print(hours, start[startPos+4:])
    if start[startPos+4:] == 'PM':
        hours = hours + 12
    print(hours)
    if hours > 24:
        while hours > 24:
            hours = hours - 24
            days = days + 1
    if hours == 24:
        days = days + 1
        hours -= 12
        s= 'AM'
    elif hours<24 and hours > 12:
        hours = hours - 12
        s = 'PM'
    elif hours == 12:
        s = 'PM'
    
    print(shours, smin, hours, min, days, s, day)
    min = str(min)
    num = days
    if int(min) < 10: min = '0'+ min
    if days > 1:
        days = ' ('+ str(days)+' days later)'
    elif days == 1:
        days = ' (next day)'
    elif days < 1: days = ''
    if day != '': 
        #print((week.index(day)+(num))%5, 'uuuuuuuu')
        day = day.lower()
        day = day.capitalize()
        day = week[(week.index(day)+(num))%7]
        day = ', '+ day
    #print(days, 'ooooo')
    return str(hours) + ':' + min + ' '+ s + day + days