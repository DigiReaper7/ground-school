import datetime as dt
name = input("What is your name? ")
d = dt.date.fromordinal(739859)
d = d.strftime("%A, %B %d, %Y")
print("Hi", name, "It's", d)
