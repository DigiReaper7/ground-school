import sys
import time


invalid_msg = "y or n only, pilot."

propellers = "Are the proplellers in good shape and properly fastened? "
propellers_n = "Tighten or replace the propellers."

batteries = "Are the batteries fully charged with no visible bluging? "
batteries_n = "Recharge or replace the batteries as needed."

notams = "Have you checked NOTAMS? "
notams_n = "Check NOTAMS."

weather = "Have you checked the weather? "
weather_n = "Check the weather first!"

sober = "Has it been at least 8 hours since your last alcoholic beverage? "
sober_n = "Make sure it's been 8 hours since your last drink."

electronics = "Are all electrnoics operating as intended? "
electronics_n = "Fix any and all elctronics issues first."


print("Preflight Safety Check")
print("Answer only with a 'y' or 'n'")

def preflight_item(question, no_go_msg):
    """Ask a  question and return the answer."""
    answer = input(question).lower()
    
    while answer != "n" and answer != "y":
        print(invalid_msg)
        answer = input(question).lower()
    if answer == "n":
        print("NO-GO.", no_go_msg)
        sys.exit()
    print("PASS")
    
preflight_item(propellers, propellers_n)
preflight_item(batteries, batteries_n)
preflight_item(notams, notams_n)
preflight_item(weather, weather_n)
preflight_item(sober, sober_n)
preflight_item(electronics, electronics_n)

for n in range(10, 0, -1):
    print(n)
    time.sleep(.5)
print("GO FOR LAUNCH")

