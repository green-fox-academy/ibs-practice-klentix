current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

hoursinsec = current_hours*3600
minsinsec = current_minutes*60
timeleft = 24*3600-(hoursinsec+minsinsec+current_seconds)
print('remaining seconds in a day:', timeleft)
