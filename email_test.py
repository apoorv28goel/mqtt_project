import smtplib

def send_mail_alert():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # print("here")
    server.starttls()
    # print("loging in")
    server.login("email.test.mqtt.alert@gmail.com", "1q2w3e4r%t")
    # print("logged in")
    msg = "Test-2"
    # print("start")
    server.sendmail("email.test.mqtt.alert@gmail.com", "apoorv28goel@live.com", msg)
    # print("exiting server")
    server.quit()


print("sending...")
send_mail_alert()
print("send")