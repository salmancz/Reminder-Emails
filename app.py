# -=-=- Developed By PyExpo Team10 -=-=- #

# Importing package
import streamlit as st
import smtplib, ssl
import random

generated_otp = random.randint(3453, 9453)
def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context = context)
        email.login(bot_email, password)
        email.sendmail(bot_email, reciever_email, main_message)


def otp_checker():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context = context)
        email.login(bot_email, password)
        email.sendmail(bot_email, reciever_email, otp_message)
        

# Getting info from user and Front-End Section
st.title("PyExpo Challenge")
st.write("Conducting grand competition for programmers. Develop your skills by challenging and solving coding problems")
st.write("We are starting soon signup for details")
st.subheader("Register")
col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("Enter your first name :")
with col2:
    second_name= st.text_input("Enter your last name :")
reciever_email = st.text_input("Email ID :")
reciever_number = st.text_input("Phone Number :")
clg_input = st.text_input("Enter your Institute : ")
send_otp_btn = st.button("Send OTP")
col3, col4 = st.columns(2)
with col3:
    input_otp = st.text_input("Enter OTP: ")
with col4:
    st.empty()
check_box = st.checkbox("I have read and accept the Terms and Conditions")
submit_button = st.button("Sign Up")


# Email Details
bot_email = "salmandev.bot@gmail.com"
password = "salmanbotpass"
port = 587
smtp_server = "smtp.gmail.com"


otp_message = """\
Subject: PyExpo - Confirm Your Email Address

Hey {}, Your otp is for regestering pyexpo is {}. 



Happy Coding!
    """.format(user_name, generated_otp)
    

main_message = """\
Subject: PyExpo is about to start!

Hey {},
Thanks for signing up. 

We are happy to inform that PyExpo is going to start in a day. Empower Your Technical Hiring Using Real-Time Coding Interviews.
Request a Demo! Scale Up Your Technical Hiring Using Our Integrated Coding Assessments and Simulators. 4000+ Clients Globally. 100K+ Questions. 
24x7 Service Support. Customized Reports. Intuitive User Interface.
for more quieries: https://salmandevee.web.app/

Happy Coding!
    """.format(user_name)
# db_list = []
# db_list.append(user_name, reciever_email)
# database = tuple()
# database.append(db_list)

# OTP Button Functionality
if send_otp_btn:
    otp_checker()
    st.write(generated_otp)
    st.success("OTP has sent!")

# Email Button Functionality
if submit_button:
    if generated_otp == int(input_otp):
        st.success("You have succesfully Signed In")
    elif generated_otp != int(input_otp):
        st.error("Can't register, OTP is incorrect")
    else:
        st.error("Check your credentials and try again")