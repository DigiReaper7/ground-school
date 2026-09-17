import sys
import time

print("Preflight Safety Check")

print("Answer only with a 'y' or 'n'")
      
propellers = input("Are the propellers in good shape and properly fastened? ").lower()
while propellers != "y" and propellers != "n":
    print("y or n only, pilot.")
    propellers = input("Are the propellers in good shape and properly fastened? ").lower()
if propellers == "n":
    print("NO-GO. Tighten or replace the propellers.")
    sys.exit()
print("PASS")
    
batteries = input("Are the batteries fully charged and with no visible bulging? ").lower()
while batteries != "y" and batteries != "n":
    print("y or n only, pilot.")
    batteries = input("Are the batteries fully charged and with no visible bulging? ").lower()
if batteries == "n":
    print("NO-GO. Recharge or replace the batteries as needed.")
    sys.exit()
print("PASS")

notams = input("Have you checked NOTAMS? ").lower()
while notams != "n" and notams != "y":
    print("y or n only, pilot.")
    notams = input("Have you checked NOTAMS? ").lower()
if notams == "n":
    print("NO-GO. Check NOTAMS.")
    sys.exit()
print("PASS")

weather = input("Have you checked the weather? ").lower()
while weather != "n" and weather != "y":
    print("y or n only, pilot.")
    weather = input("Have you checked the weather? ").lower()
if weather == "n":
    print("NO-GO. Check the weather first!")
    sys.exit()
print("PASS")

sober = input("Has it been at least 8 hours since your last alcoholic beverage? ").lower()
while sober != "n" and sober != "y":
    print("y or n only, pilot.")
    sober = input("Has it been at least 8 hours since your last alcoholic beverage? ").lower()
if sober == "n":
    print("NO-GO. Make sure it's been 8 hours since your last drink.")
    sys.exit()
print("PASS")

electronics = input("Are all electronics operating as intended? ").lower()
while electronics != "n" and electronics != "y":
    print("y or n only, pilot.")
    electronics = input("Are all electronics operating as intended? ").lower()    
if electronics == "n":
    print("NO-GO. Fix any and all electronics issues first.")
    sys.exit()
print("PASS")

for n in range(10, 0, -1):
    print(n)
    time.sleep(.5)
print("GO FOR LAUNCH")

