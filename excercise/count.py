import datetime
import time

# a simple program that allows the user to pick a time and the program counts down
# until that time has been reached

month_strings = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec',]

# This function creates a datetime object chosen by the user and compares
# this object to the current time and counts down until that chosen time
def count_down():


    year = int(raw_input('What is the year of the date? '))
    month = raw_input('What is the month of the date? ')
    # this part allows the user to type in the month as a string or integer
    if len(month) < 3:
        month = int(month)
    else:
        month = (month_strings.index(month[0:3].lower()) + 1)
    day = int(raw_input('What is the day of the month? '))
    hour = int(raw_input('What is the hour according to a 24 hour clock? '))
    minute = int(raw_input('At which minute? '))
    second = int(raw_input('At which second? '))

    chosen_time = datetime.datetime(year,month,day,hour,minute,second)

    print 'The time you chose is: ' + chosen_time.__str__()

    current_time = chosen_time.now()
    # If the time has passed, let the user know and exit the program
    if chosen_time < chosen_time.now():
        print 'This time has passed.'
        exit()

    else:
        # This loop prints how much time is left until the chosen time every 3 seconds
        while True:
            time_difference = (chosen_time - chosen_time.now())
            print str(time_difference)

            time.sleep(1)
            if chosen_time <= chosen_time.now():
                break
        print "It's time!"
        exit()

if __name__ == '__main__':
    count_down()
