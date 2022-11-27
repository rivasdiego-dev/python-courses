import random
# The max and min functions give us the largest and smallest values in a list
max('Hello world')
min('Hello world')

# len function which tells us how many items are in its argument.
len('Hello world')

# Python also provides built-in functions that convert values from one type to another
int(3.99999)
int(-2.3)

# This part produces a list of 10 random numbers between 0.0 and up to but not including 1.0. ******* You have to import random ********
for i in range(10):
  x = random.random()
  print(x)

# randint takes the parameters low and high, and returns an integer between low and high
random.randint(5, 10)

# To choose an element from a sequence at random, you can use choice
t = [1, 2, 3]
random.choice(t)


# TO ADD FUNCTIONS
# def is a keyword that indicates that this is a function definition
def print_default_motd():
  print("Hello World!")

def get_def_motd():
  return "Hello World!"
  
def print_motd(motd):
  print(motd)

print_default_motd()
print(get_def_motd())
print_motd("Hey World!")
print_motd("Sup World!")
