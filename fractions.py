print('Calculate the following fractions: 1/2 + 5/6. Simplify your answer as necessary.')
answer = input('Enter your answer: ')
if answer == '4/3':
  print('Correct!')
elif answer == '6/8':
  print('Based on your answer, it appears you forgot the lowest common denominator.')
  answer1 = input('What number is the least common multiple between 2 and 6? ')
  for i in answer1:
    if answer1 != 6:
      print('Try again.')
    elif answer1 == 6:
      print('Correct! Now you can return to the original problem.')
