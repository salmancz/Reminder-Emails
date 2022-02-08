import streamlit as st
import smtplib, ssl

bot_email = "salmandev.bot@gmail.com"
password = "salmanbotpass"
port = 587
smtp_server = "smtp.gmail.com"

def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context = context)
        email.login(bot_email, password)
        email.sendmail(bot_email, reciever_email, main_message)

st.title("Admin Home")
st.subheader("Mail Context")
st.empty()
st.write("""
         
Subject: PyExpo is about to start!

Hey,
Thanks for signing up. 

We are happy to inform that PyExpo is going to start in a day. Empower Your Technical Hiring Using Real-Time Coding Interviews.
Request a Demo! Scale Up Your Technical Hiring Using Our Integrated Coding Assessments and Simulators. 4000+ Clients Globally. 100K+ Questions. 
24x7 Service Support. Customized Reports. Intuitive User Interface.
for more quieries: https://salmandevee.web.app/

Happy Coding!""")
st.button("Send Mail")