# Declaring variables
max = sum = total_numbers = 0
min = 10000

while True: # Entering an infinite loop
  try: # Avoiding errors
    user_input = input('Enter a number: ') # Asking for a number
    if user_input == 'done': break # If user won't add more numbers
    user_input = int(user_input) # Parsing data to int
    if user_input < min: min = user_input # Changing min amount
    if user_input > max: max = user_input # Changing max amount
    total_numbers += 1 # Adding one to the counter
    sum += user_input # Adding the user input to the total
  except:
    print('Invalid input')
    continue

print('Numbers count: ',total_numbers, '\tTotal sum: ', sum, '\nMax: ', max, '\tMin: ', min)