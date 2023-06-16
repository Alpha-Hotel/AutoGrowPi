import smtplib
from os import environ as e
# https://testingonprod.com/2021/10/24/how-to-send-text-messages-with-python-for-free/
def test_message(phone_number, carrier):
    recipient=phone_number+carrier
    auth = ("ahparadox2159@gmail.com", e['APPLICATION_KEY'])
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    server.sendmail(auth[0], recipient, "This is a messages testing the automatic alarm messaging system.")

if __name__ == "__main__":
    print(dict(e))
    test_message("8452393910","@tmomail.net")