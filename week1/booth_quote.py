booth_rate = 150
backdrop_rate = 75
addon_rate = 25
distance_fee = 50

hours_needed = input("How many hours do you need the booth? ")
hours_needed = int(hours_needed)

event_distance = input("How many miles from Chicago is your event? ")
event_distance = int(event_distance)

add_ons = input("How many add-ons? ")
add_ons = int(add_ons)

backdrop_bool = input("Do you need the backdrop? yes or no ")

total_booth_price = booth_rate * hours_needed

total_backdrop_price = backdrop_rate * hours_needed

total_addon_price = addon_rate * add_ons

grand_total =  total_booth_price + total_backdrop_price + total_addon_price

print(f"Your quote total is: ${grand_total:.2f}")