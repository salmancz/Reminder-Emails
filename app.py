# # -=-=- Developed By PyExpo Team10 -=-=- #

# # Importing package
import streamlit as st
import smtplib, ssl
import datetime as dt
import time

# Getting info from user and Front-End Section
st.title("PyExpo Challenge")
st.write("Conducting grand competition for programmers. Develop your skills by challenging and solving coding problems")
st.write("We are starting soon signup for details")
user_name = st.text_input("Enter your name :")
reciever_email = st.text_input("Email ID :")
submit_button = st.button("Sign Up")


# Email Details
bot_email = "salmandev.bot@gmail.com"
password = "salmanbotpass"
port = 587
smtp_server = "smtp.gmail.com"

message = """\
Subject: PyExpo is about to start!

Hey {},
Thanks for signing up. 

We are happy to inform that PyExpo is going to start in a day. Empower Your Technical Hiring Using Real-Time Coding Interviews.
Request a Demo! Scale Up Your Technical Hiring Using Our Integrated Coding Assessments and Simulators. 4000+ Clients Globally. 100K+ Questions. 
24x7 Service Support. Customized Reports. Intuitive User Interface.
for more quieries: https://salmandevee.web.app/

Happy Coding!
    """.format(user_name)


# Button Functionality
if submit_button:
    st.success("You have succesfully signed in")
    # Email Functionality 
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context = context)
        email.login(bot_email, password)
        send_time = dt.datetime(2022, 1, 5, 14, 43, 00)
        x = time.sleep(send_time.timestamp() - time.time())
        email.sendmail(bot_email, reciever_email, message)

