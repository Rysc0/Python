#sending email with python

# from smtplib import SMTP
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ctrlwin99@gmail.com"  # Enter your address
receiver_email = "ctrlwin99@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

cont = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=cont) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

# import smtplib
# sender_email = "ctrlwin99@gmail.com"
# passw = input("Gimme pass: ")
# receiver_email = "rpfhbsuoqkvivdztyd@wqcefp.online"
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(sender_email, passw)
# server.sendmail(
#   sender_email, 
#   receiver_email, 
#   "this message is from python")
# server.quit()


