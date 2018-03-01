#Marco Men's week 3-Collatz Sequence
raw_input = int(input('Enter a number, please:'))
number = raw_input
steps = 0   #<--- Loop begins here
while number > 1:
      if number % 2 == 0:
         number = number / 2
         print(number)   #<--- For even numbers,print
      else:     #<---Non-even=Odd
         number = number * 3 + 1
         print(number) #<--For odd numbers,print

      steps += 1  #<---add 1 after the loop,otherwise it will continue running continuously
#{}.format (steps)) adapted from: 'https://docs.python.org/3/library/stdtypes.html#str.format'
print('%s' % (raw_input) ,'took {}'.format(steps)) , 'steps'
