

def convert(hours, minutes):
    #write some code to convert hours to seconds and minutes to seconds
    hours_to_seconds = (60 * hours)*60
    minutes_to_seconds = 60 * minutes

    seconds = minutes_to_seconds + hours_to_seconds

    return seconds

print (convert(10,10))