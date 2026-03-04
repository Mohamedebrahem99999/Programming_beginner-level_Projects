import random
import string

def main():
  password_list = []
  print("Welcome to the password generator! ")
  password_len = int(input("Enter the password length to be generated "))
  letters_num = int(input("Enter the number of alphabet letters your password "))
  numbers_num = int(input("Enter the number of numbers in your password "))
  symbol_numbers = int(input ("Enter the number of symbols in your password "))

  while letters_num + numbers_num + symbol_numbers != password_len:
    print("Invaid input, the sum of letters, numbers and symbols doesn't match the password length")
    password_len = int(input("Enter the password length to be generated "))
    letters_num = int(input("Enter the number of alphabet letters your password "))
    numbers_num = int(input("Enter the number of numbers in your password "))
    symbol_numbers = int(input ("Enter the number of symbols in your password "))
  else:
      letters = random.choices(string.ascii_letters, k=letters_num)
      password_list = [i for i in letters]    
      numbers = random.choices(string.digits, k=numbers_num)
      for x in numbers :
        password_list.insert(random.randint(0,4),x)
      symbols = random.choices(string.punctuation, k=symbol_numbers)
      for z in symbols:
        password_list.insert(random.randint(0,7),z)
      password = "".join(password_list)
      print("Generated password: ", password)
main()
  