import random
  
def main():
    
  dice_sum = 0
  dice_rolls = int(input("How many dice?"))
  dice_size = int(input("How many sides?"))

  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f"You rolled a {roll}! Critical fail!")
    elif roll == dice_size:
      print(f"A {roll}! Woop!")  
    else:
      print(f"You rolled a {roll}")

  print(f"You rolled a total of {dice_sum}")


if __name__== "__main__":
  main()