booth_rate_hourly = 150
backdrop_rate_hourly = 75
add_on_rate = 25
distance_fee = 50

def base_price():
    hours_needed = input("How many hours do you need the booth? ")
    hours_needed = int(hours_needed)
    total_base_price = hours_needed * booth_rate_hourly
    return total_base_price

def travel_fee():
    event_distance = input("Is your event more than 50 miles from Chicago? ").lower()
    while event_distance != "n" and event_distance != "y":
        print("Invalid Answer. Use only 'y' or 'n'")
        event_distance = input("Is your event more than 50 miles from Chicago? ").lower()
    if event_distance == "y":
        return(50)
    else:
        return(0)

def add_ons():
    add_ons = input("How many add-ons? ")
    add_ons = int(add_ons)
    total_add_on_price = add_ons * add_on_rate
    return total_add_on_price

def quote(base_price, travel_fee, add_ons):
    total_price = base_price + travel_fee + add_ons
    print(f"Your quote total is: ${total_price}")


total_base_price = base_price()

distance_price = travel_fee()

total_add_on_price = add_ons()

quote(total_base_price, distance_price, total_add_on_price)