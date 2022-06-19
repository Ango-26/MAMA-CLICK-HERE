import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

#dont 4 get to enable the 3rd party apps access on palace of zen google account



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('palaceofzen@gmail.com', 'sevenholt0903!')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'anish.golikere@tts.edu.sg',
    'rao': 'raosg2019@gmail.com',
    'ram': 'ramgr100@yahoo.com',
    'abhay': 'abhay.golikere@tts.edu.sg',
    'anish': 'anishgolikere@gmail.com'
}


def get_email_info():
    talk('To Whom do you want to send this email to?')
    name = input("Name: ")
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = input("Subject: ")
    talk('Tell me the text you want in your email')
    message = input("Context: ")
    send_email(receiver, subject, message)
    talk('Ok buddy. Your email has been sent')
    talk('Do you want to send more emails?')
    send_more = input("yes or no?: ")
    if 'yes' in send_more:
        get_email_info()
    else:
        quit()


get_email_info()