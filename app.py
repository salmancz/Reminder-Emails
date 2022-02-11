# -=-=- Developed By PyExpo Team10 -=-=- #

# Importing package
import streamlit as st
import smtplib, ssl 
import random
import csv

# Email Details
bot_email = "salmandev.bot@gmail.com"
password = "salmanbotpass"
port = 587
smtp_server = "smtp.gmail.com"

# Getting info from user and Front-End Section
st.title("PyExpo Challenge")
st.write("Conducting grand competition for programmers. Develop your skills by challenging and solving coding problems. Enhance your skills with these new and easy problems.")
st.write("We are starting soon signup for details")
st.subheader("Register")
col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("Enter your first name :")
with col2:
    second_name= st.text_input("Enter your last name :")
filename = "otp_file.csv"
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
    for row in rows:
        for col in row:
            hidden_otp = col.replace(" ", "")
otp_message = """\
    Subject: PyExpo Verify Your Email

    Hey {},
    Confirm your email address by entering this OTP = {}
    If it's not you Kindly ignore this

    Happy Coding!
        """.format(user_name, hidden_otp)
reciever_email = st.text_input("Email ID :")
reciever_number = st.text_input("Phone Number :")
clg_input = st.text_input("Enter your Institute : ")
send_otp_btn = st.button("Send OTP")
if send_otp_btn:
    otp_database = []
    otp_details = (str(random.randint(3452, 9354)))
    otp_database.append(otp_details)
    with open ('otp_file.csv','a',newline = '') as csvfile:
        otp_writer = csv.writer(csvfile, delimiter = ' ')
        otp_writer.writerows(otp_database)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context = context)
        email.login(bot_email, password)
        email.sendmail(bot_email, reciever_email, otp_message)
    
    st.success("OTP has sent!")
col3, col4 = st.columns(2)
with col3:
    get_otp = st.text_input("Enter OTP: ")
with col4:
    st.empty()
check_box = st.checkbox("I have read and accept the Terms and Conditions")
submit_button = st.button("Sign Up")
    

# OTP Button Functionality
if submit_button:
    member_database = []
    member_details = (user_name, reciever_email)
    member_database.append(member_details)
    with open ('members.csv','a',newline = '') as csvfile:
        otp_writer = csv.writer(csvfile, delimiter = ' ')
        otp_writer.writerows(member_database)
    filename = "otp_file.csv"
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    result = False
    for row in rows:
        for col in row:
            hidden_otp = col.replace(" ", "")
            if hidden_otp == str(get_otp):
                st.success("OTP Verified")
                result = True
    if result == False:
        st.error("Incorrect OTP, Try again later")
