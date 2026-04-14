#QuestionsAboutYourself
import math
import numbers

print("Hi there what is your name?")
yourName = input()
print(f"Hi {yourName} how old are you?")
yourAge = input("Your age:")
try:
 val = int(yourAge)
except ValueError:
 print("Thats not a number!")
if(val < 18):
 print("You're not an adult correct?")
 ageConf = input()
 if(ageConf == "yes"):
  print("Imagine still having to go through school lol.")
 elif(ageConf == "no"):
  print("Wait if my math is mathing you should be a kid your weird.")
  print("Well now you're being mean bye now.")
elif(val > 18):
 print("You are an adult correct?")
 ageConf = input()
 if(ageConf == "no"):
  print("Wait if my math is mathing you should be a adult your weird.")
  print("Well now you're being mean bye now.")
 elif(ageConf == "yes"):
  print("Wow you can have alchohol right?")
  alcConf = input()
  if(alcConf == "yes"):
   print("Can you buy me some?")
  elif(alcConf == "no"):
   print("You can't buy alchohol? Nah you big liar.")
   print("Well now you're being mean bye now.")