import datetime

# Get current date and time
now = datetime.datetime.now()

# Display current date and time
print("Current date and time:", now)

# Get and display day of the week
day_of_week = now.strftime("%A")
print("Day of the week:", day_of_week)
