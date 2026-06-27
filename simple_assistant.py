# simple voice assistant (text version)

import datetime

while True:
    command = input("Enter command: ").lower()

    if command == "time":
        print("Current Time:",
              datetime.datetime.now().strftime("%H:%M:%S"))
    elif command =="date":
        print("Today's Date:",
              datetime.date.today())
    elif command == "date time":
        print("Date/Time:",
              datetime.date.today(),datetime.datetime.now().strftime("%H:%M:%S"))
    elif command =="hello":
        print("Hello!\nHow are You")
    elif command =="bye":
        print('Goodbye!')
        break
    else:
        print("Command Not Found")
