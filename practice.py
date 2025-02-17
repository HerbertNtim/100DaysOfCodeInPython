print("Welcome to FizzBuzz")
for i in range(1, 101):
  if i % 5 == 0 and i % 3 == 0:
    print('FizzBuzzz', i)
  elif i % 3 == 0: 
    print("Fizz", i)
  elif i % 5 == 0:
    print('Buzz', i)
  else:
    pass
