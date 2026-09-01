import datetime as dt
name = input("What is your name? ")
today = dt.date.today()
today = today.strftime("%A, %B %d, %Y")
print("Hi", name, "It's", today)
