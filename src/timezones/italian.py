def time_conversion_italian(utc_time_str, types, month):
    if types == "identifier":
        if utc_time_str != "NA":
            utc_time = datetime.datetime.strptime(utc_time_str, '%b %d %Y %H:%M')
            utc_tz = pytz.timezone('UTC')
            utc_time = utc_tz.localize(utc_time)
            italian_tz = pytz.timezone('Europe/Rome')  # Italian timezone based on pytz timezone list
            italian_time = utc_time.astimezone(italian_tz)
            italian_time_str = italian_time.strftime("%b %d %Y %H:%M")
            return italian_time_str
        
    else:
        if month == "october2march":   # untested
            utc_tz = pytz.timezone('UTC')
            italian_tz = pytz.timezone('Europe/Rome')  # Italian timezone (winter time) UTC+1
            utc_time = datetime.datetime.strptime(utc_time_str, '%Y-%m-%d %H:%M:%S')
            utc_time = utc_tz.localize(utc_time)
            italian_time_str = utc_time.astimezone(italian_tz)
            return italian_time_str
            
        elif month == "march2october":   # untested
            utc_tz = pytz.timezone('UTC')
            italian_tz = pytz.timezone('Europe/Athens')  # Italian timezone (daylight saving) UTC+2
            utc_time = datetime.datetime.strptime(utc_time_str, '%Y-%m-%d %H:%M:%S')
            utc_time = utc_tz.localize(utc_time)
            italian_time_str = utc_time.astimezone(italian_tz)
            return italian_time_str
###
#/ Last modified: 14 July 2024
#/ Repo owner: dasabhijeet.com
