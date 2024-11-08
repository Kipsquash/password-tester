#Python script that allows you to input a password and it will test the strength of the password 

import pyperclip
from passwordlib import util as pwutil
from passwordlib.commonly_used import is_commonly_used
from passwordlib.analyzer import Analyzer




password = input("Input your password here: ")
pass_len = len(password)

result=Analyzer(password)
print(result.is_secure)
print(result.is_highly_secure)
print(result.score) 
while True:
   if result.is_secure:
       if result.is_highly_secure:
           print("Password is highly secure! ")
           print("Your password score is a " + result.score + "out of 10.")
       else:
           print("Your password is secure but could be better! do you want to try again?")
   

    
# number_of_security_features = sum((
#   result.contains_lowercase,
#   result.contains_uppercase,
#   result.contains_digits,
#   result.contains_symbols,
#   result.length >= 8,
#   result.charset_length > (result.length // 2)
# ))
# if number_of_security_features < 5 or result.is_commonly_used:
#   raise (result.password)
   

   
   
   
   
   
   
   
   

pyperclip.copy(password)
print("Your password is copied to your clipboard")
print("Dont forget to keep it safe! Enjoy!")