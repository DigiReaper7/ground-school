volts = float(input("What is your cell's voltage? "))

while volts < 0 or volts > 4.5:
    print(f"Try again friend. Not a valid cell voltage.")
    volts = float(input("What is your cell's voltage? "))

if volts <= 3.00:
    print(f"DANGER - @ {volts:.2f} volts. Better hope it still works!!!")
elif volts <= 3.60:
    print(f"Discharged to {volts:.2f} volts. Recharge to a safe level.")
elif volts <= 3.84:
    print(f"@ - {volts:.2f} volts. Recharge needed.")
elif volts <= 3.85:
    print(f"@ - {volts:.2f} volts. Ready for storage.")
elif volts <= 4.19:
    print(f"@ - {volts:.2f} volts. Recharge to 4.2V")
elif volts <= 4.20:
    print(f"@ - {volts:.2f} volts. Ready to rock n' roll!!!")
elif volts <= 4.5:
    print(f"DANGER @ - {volts:.2f} VOLTS!!! DANGER - DISCHARGE TO A SAFE LEVEL NOW!!!")
else:
    print("Bruh...for real?!?!?!")
