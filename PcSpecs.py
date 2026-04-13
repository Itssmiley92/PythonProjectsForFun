#What are your PC Specs?
from time import sleep

print("What brand of computer do you have?")
comBrand = input()
print(f"So the brand of the computer is {comBrand}?")
comBrandConf = input()
while(comBrandConf == "no" or comBrandConf == "nein"):
 print("What brand of computer do you have?")
 comBrand = input()
 print(f"So the brand of the computer is {comBrand}?")
 comBrandConf = input()
 if(comBrandConf == "yes"):
  print("What is the processor?")
  cpuType = input()
  print(f"You have a {cpuType} nice!")
  print("What is the graphics card?")
  gcardType = input()
  print(f"A {gcardType} that must be a good card!")
  print("How much ram do you have (gbs) and what type? (ddr5/ddr4)")
  ramTypeGb = input()
  print(f"You have {ramTypeGb} you must be rich!")
  print("How much storage do you have? (gb/tb)")
  storageAmount = input()
  print(f"Wow you have {storageAmount}!")
  sleep(1)
  print(f"So in total you have a {comBrand} with a {cpuType}, {gcardType}, {ramTypeGb}, and {storageAmount}'s of storage thats a nice Pc!")