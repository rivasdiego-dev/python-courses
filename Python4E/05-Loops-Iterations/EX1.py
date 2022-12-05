total_numbers = 0
average = 0
sum = 0

while True:
  try:
    user_input = input('Enter a number ')
    if user_input == 'done': break
    user_input = int(user_input)
    total_numbers += 1
    sum += user_input
  except:
    print('Bad input')
    continue

average = sum / total_numbers

print('Numbers count: ',total_numbers, '\nTotal sum: ', sum, '\nAverage: ', average)