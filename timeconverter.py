

##importing a regular expressions module that comes with python
import re

def convert_to_24hour(time_str):
##a function that takes time string as an argurment
    hour, minute, second, am_pm = re.findall('\d+|\w+', time_str)

    ##checks if they is digits or words in the time string AM/PM
    hour = int(hour)
    ##converting hour to an interger 

    if am_pm == 'PM' and hour != 12:
        hour += 12
        ## if not 12 convert it to 24 hrs
    elif am_pm == 'AM' and hour == 12:
        hour = 0

    return f'{hour:02d}:{minute}'

print(convert_to_24hour('11:21 PM'))
print(convert_to_24hour('12:12 AM'))

