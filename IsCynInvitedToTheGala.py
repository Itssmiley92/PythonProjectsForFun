# Is Cyn Invited to the Gala
from itertools import count
import os
from time import *

print("Am i inv-v-vited t0 the g-g-gala?")
cynInvited = input()
while (cynInvited == "no" or cynInvited == "nein"):
 print("0k w-well h0-w-w many pe0pl-e-e are here?")
 cynKillCount = input()
 print(f"S-s0 there-e ar-e {cynKillCount} pe0ple he-ere?")
 if(cynKillCount == "no" or cynKillCount == "0"):
  print("N-n0 pe0ple a-awwwww")
  break
 elif(cynKillCount == "yes"):
  print("Wait Cyn confuzled")
  sleep(1)
  print("Cyn.exe loading...")
  sleep(5)
  print("Cyn.exe crashed from too much thinking 💀")
  break
 cynConfirmation = input()
 if(cynConfirmation == "yes"):
  print("EV-V-VERY0N-N-NE D-D-DIES N0-0-W 🔪🩸")
  sleep(1)
  count = 0
  while count < 20:
   os.system("start cmd /k echo YOU'RE DEAD")
   count += 1
  break
 elif(cynConfirmation == "no"):
  print("H-ey thats me-ean y0-u m-made m-me sad 😭")
  sleep(1)
  print("Y0u-u DIE n-n0w")
  break
if(cynInvited == "yes"):
 print("Cyn happy 😊")
