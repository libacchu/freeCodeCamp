import math

def add_time(start, duration, day = None):
    new_time = ""
    # Split the start time into hours, minutes, and period 
    start_time = start.split()
    start_hour = int(start_time[0].split(":")[0])
    start_min = int(start_time[0].split(":")[1])
    start_period = start_time[1]

    # Split the duration into hours and minutes
    duration_hour = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])

    # Calculate the new time
    new_hour = start_hour + duration_hour
    
    new_min = start_min + duration_min

    if new_min > 59:
        new_hour += new_min // 60
        new_min = new_min % 60

    # Calculate the number of days later
    days_later = math.floor(new_hour / 24)

    # Calculate the new period
    new_period = start_period
    if (new_hour % 24) >= 12:
        new_hour = new_hour % 12
        if new_hour == 0:
            new_hour = 12
        if start_period == "AM":
            new_period = "PM"
        else:
            new_period = "AM"
            days_later += 1
    else:
        new_hour = new_hour % 12
        if new_hour == 0:
            new_hour = 12

    # Format the new time  
    new_time = str(new_hour) + ":" + str(new_min).zfill(2) + " " + new_period

    # Add the day of the week if it was provided
    if day != None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        new_day = days[(days.index(day.lower().capitalize()) + days_later) % 7]
        new_time += ", " + new_day
    
    # Add the number of days later if it was provided
    if days_later > 0:
        if days_later == 1:
            new_time += " (next day)"
        else:
            new_time += " (" + str(days_later) + " days later)"

    # print("start:\t\t", start_time, "\nnew hour:\t", new_hour, "\nnew min:\t", new_min, "\nnew period:\t", new_period, "\ndays later:\t", days_later)

    return new_time
