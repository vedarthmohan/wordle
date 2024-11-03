import random
from colorama import Fore
import os

os.system('clear')
print ("We are playing Wordle.")

def get_dict():
   with open("/usr/share/dict/words", 'r') as file:
      dict = file.read()
   dict_list = []
   dict_list = dict.split()
   dict_5 = []
   for s in dict_list:
      if len(s)==5:
         dict_5.append(s)
   return(dict_5)

if __name__ == '__main__':
   wordle_dict = get_dict()
   random_number = random.randint(0, len(wordle_dict)-1)
  # print(wordle_dict[random_number])
   print("Lets start guessing! 6 tries! ")

   print("Guess a 5 character secret code from the alphabet. \n Blue is for character in right place. \n Red for character present in secret, but wrong place")

   test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

   # assign secret to the newly picked random word.
   secret = (wordle_dict[random_number]).lower()

   chances = 6
   while (chances > 0):
      guess=input().lower()
   
      # Is guess a real word?
      if (guess not in wordle_dict):
         print(guess + " is not a valid word. Try doesnt count")
         continue
      
      chances = chances - 1 # same as chances--
      guess_output = ""
      i = 0
      green = 0
      yellow = 0
      for i in range(len(guess)):
         if (guess[i] in list(secret)): # is character in secret?

            if (guess[i] == secret[i]): # is character in correct position in secret?
               green = green + 1;
               guess_output = guess_output + f"{Fore.LIGHTCYAN_EX}" + guess[i]

            else:
               yellow = yellow + 1;
               guess_output = guess_output + f"{Fore.LIGHTRED_EX}" + guess[i]

         else:
            guess_output = guess_output + f"{Fore.LIGHTWHITE_EX}" + guess[i]
      print("\n Good guess " + str(6 - chances) + ". You got " + guess_output + f"{Fore.RESET}" + "\n")

      if(guess == secret):
         print("You win!!!!")
         break

   if (guess != secret):
      print("You Lost :( Secret was : " + secret)

   print("Game over!")
