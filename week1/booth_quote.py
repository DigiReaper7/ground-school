boothRate = 150
backdropRate = 75
addOnRate = 30
distanceFee = 50

hoursNeeded = input("How many hours do you need the booth? ")
hoursNeeded = int(hoursNeeded)

eventDistance = input("How many miles from Chicago is your event? ")
eventDistance = int(eventDistance)

addOns = input("How many add-ons? ")
addOns = int(addOns)

backdropBool = input("Do you need the backdrop? yes or no ")
backdropBool = bool(backdropBool)

totalBoothPrice = boothRate * hoursNeeded

totalBackdropPrice = backdropRate * hoursNeeded

totalAddOnPrice = addOnRate * addOns * hoursNeeded

grandTotal =  totalBoothPrice + totalBackdropPrice + totalAddOnPrice

print(f"Your total quote is: ${grandTotal}")