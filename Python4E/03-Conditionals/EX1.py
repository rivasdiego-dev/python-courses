#Asking to the user for the necessary data and declaring vars
hours_worked = input("Please, enter hours worked: ")
hourly_rate = input("Please, enter pay rate: ")
total_payment = 0.0

# Converting input strings to floats to work w/them
hours_worked = float(hours_worked)
hourly_rate = float(hourly_rate)

if hours_worked > 40: # If employee worked overtime
  total_payment = (40 * hourly_rate) + (hours_worked - 40) * (1.5 * hourly_rate)
  # His/her payment wil be the hourly rate stablished from 0 to 40 plus
  # the amount of hours made on overtime (1.5 times the original rate)
  print("The employee worked overtime.")
else: # Employee worked 40 hours or less
  total_payment = hours_worked * hourly_rate
  print("The employee didn't worked overtime.")

print("Payment for the eployee: ", total_payment)
