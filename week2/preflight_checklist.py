import sys
import time

print("Preflight Safety Check")

print("Answer only with a 'y' or 'n'")
      
propellers = str(input(f"Are the propellers in good shape and properly fastened? "))
while propellers == "n":
    print(f"NO-GO. Tighten or replace the propellers as needed and try again.")
    sys.exit()
if propellers == "y":
    print("PASS")
else:
    print(f"Not a valid selection. Try again")
    propellers = str(input(f"Are the propellers in good shape and properly fastened? "))
    while propellers == "n":
        print(f"NO-GO. Tighten or replace the propellers as needed and try again.")
        sys.exit()
    if propellers == "y":
        print("PASS")

    
batteries = str(input("Are the batteries fully charged and with no visible bulging? "))
while batteries == "n":
    print(f"NO-GO. Recharge or replace the batteries as needed and try again.")
    sys.exit()
if batteries == "y":
    print("PASS")
else:
    print(f"Not a valid selection. Try again")
    batteries = str(input("Are the batteries fully charged and with no visible bulging? "))
    while batteries == "n":
        print(f"NO-GO. Recharge or replace the batteries as needed and try again.")
        sys.exit
    if batteries == "y":
        print("PASS")

notams = str(input("Have you checked NOTAMS? "))
while notams == "n":
    print(f"NO-GO. Check NOTAMS and try again.")
    sys.exit
if notams == "y":
    print("PASS")
else:
    print(f"Not a valid selection. Try again")
    while notams == "n":
        print(f"NO-GO. Check NOTAMS and try again.")
        sys.exit
    if notams == "y":
        print("PASS")

weather = str(input("Have you checked the weather? "))
while weather == "no":
    print(f"NO-GO. Check the weather and try again.")
    sys.exit
if weather == "y":
    print("PASS")
else:
    print(f"Not a valid selection. Try again")
    while weather == "no":
        print(f"NO-GO. Check the weather and try again.")
        sys.exit
    if weather == "y":
        print("PASS")

sober = str(input("Has it been at least 8 hours since your last alcoholic beverage? "))
while sober == "no":
    print(f"NO-GO. Make sure it's been 8 hours since your last drink and try again.")
    sys.exit
if sober == "y":
    print("PASS")
else:
    print(f"Not a valid selection. Try again")
    while sober == "no":
        print(f"NO-GO. Make sure it's been 8 hours since your last drink and try again.")
        sys.exit
    if sober == "y":
         print("PASS")

electronics = str(input("Are all electronics operating as intended? "))
while electronics == "n":
    print(f"NO-GO. Fix any and all electronics issues and try again.")
    sys.exit
if electronics == "y":
    print("PASS")
else:
    print(f"Not a valid selection. Try again")
    while electronics == "n":
        print(f"NO-GO. Fix any and all electronics issues and try again.")
        sys.exit
    if sober == "y":
        print("PASS")

for n in range(10, 0, -1):
    print(n)
    time.sleep(1)
print(f"GO FOR LAUNCH")

