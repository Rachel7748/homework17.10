import random

def lucky_num ():
    x=random.randint(1,10)
    num=int(input('please enter a number betweeen 1-10'))
    while num != x:
     num= int(input('please enter a number betweeen 1-10'))
     if num < x:
      print('too low')
     elif num > x:
      print('too high')
     else:
          print('bingo')
lucky_num()

