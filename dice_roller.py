import random
def main():
  dicesides = int(input('enter the number of sides of dice- '))
  dice_to_roll = int(input('how many dice you want to roll?'))
  nsum = 0
  for i in range(dice_to_roll):
    print('You rolled dice no '+str(i+1))
    n = random.randint(1,dicesides)
    print('Congratulations..! you got ' + str(n))
    nsum += n
  print('you got total of '+str(nsum))
  print('Thank you')

if __name__== "__main__":
  main()