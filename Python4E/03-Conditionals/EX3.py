# Asking the user for the score to evaluate
score = input("Please, enter the score: ")


# Try-catch statement to avoid solution end with error

try:
  score = float(score) # Parsing text to float

  # Making all validations
  if score >=0.9:
    print("A")
  elif score >=0.8:
    print("B")
  elif score >=0.7:
    print("C")
  elif score >=0.6:
    print("D")
  elif score <0.6:
    print("F")
  else:
    print("Invalid score...")
except:
  print("The input was invalid. Make sure to use only numbers")