# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.

workdays = 5
weeks = 17
hours = 6

TotalHoursPerSememster = (hours*workdays*weeks)
print ('TotalHoursPerSememster =',TotalHoursPerSememster )

# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

workhoursweekly = 52
#workdays = 5
#hours2 = (workhoursweekly/workdays)
#print (hours2)
TotalHoursPerSememster2Perc = (workhoursweekly * weeks / TotalHoursPerSememster * 100)
print ('TotalHoursPerSememster2Perc=',TotalHoursPerSememster2Perc)