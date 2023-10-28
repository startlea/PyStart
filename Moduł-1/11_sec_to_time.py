import datetime

second = int(input("How many seconds you want to convert into time? "))

print(str(datetime.timedelta(seconds=second)))

#Another way of doing things
seconds = int(input("Give me time in seconds: "))
while seconds > 86400:
    seconds -= 86400
hour = seconds // 3600
minutes = seconds % 3600 / 60

print(f"{hour:02.0f}:{minutes:02.0f}")