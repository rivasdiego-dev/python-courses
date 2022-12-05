total_numbers = 0

while True:
  try:
    list[total_numbers] = int(input('Enter a number'))
  except:
    print('Bad input')
  